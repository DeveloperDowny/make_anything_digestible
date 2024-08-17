from fastapi import FastAPI
from pydantic import BaseModel

from app.random_striver_sheet_question_opener.v2 import SheetHandlerFactory, SheetHandler
from app.llm_service import LLMService
from app.config.config import Config

import os
from dotenv import load_dotenv

load_dotenv()

import httpx
from fastapi import Request, HTTPException

import json
import logging

from app.html_extractor import extract_html

app = FastAPI()
llm_service = LLMService(api_key=Config.OPEN_AI_KEY)

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
SENDER_NAME = os.getenv("SENDER_NAME")

if not BREVO_API_KEY or not SENDER_EMAIL or not SENDER_NAME or not RECEIVER_EMAIL:
    raise EnvironmentError("Missing environment variables")

isdm = Config.DEBUG
# isdm = False


def dummy_send_email_request(subject: str, html_content: str) -> httpx.Response:
    # console
    print(f"Email subject: {subject}")
    print(f"Email content: {html_content}")
    return httpx.Response(200, json={"message": "Email sent successfully"})


async def send_email_request(subject: str, html_content: str) -> httpx.Response:
    if isdm:
        return dummy_send_email_request(subject, html_content)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "Accept": "application/json",
                "Api-Key": BREVO_API_KEY,
                "Content-Type": "application/json",
            },
            json={
                "sender": {"email": SENDER_EMAIL, "name": SENDER_NAME},
                "to": [{"email": RECEIVER_EMAIL}],
                "subject": subject,
                "htmlContent": html_content,
            },
        )
    return response


logger = logging.getLogger(__name__)


def process(self):
    result = {}
    with open(self.data_file_path, "r") as file:
        data = json.load(file)
    with open(self.history_file_path, "r") as file:
        history = json.load(file)["solved_ids"]

    flattened = self.flatten(data)
    filtered_data = self.remove_solved(flattened, history)
    random_topic = self.get_random_topic(filtered_data)
    result["topic"] = random_topic
    id = random_topic["id"]

    logger.info(f"Selected topic: {json.dumps(random_topic, indent=2)}")
    link = self.create_link(self.get_title(random_topic))
    logger.info(f"Link: {link}")
    self.update_history(history, id)
    return result


@app.get("/random_question/{sheet_type}")
async def random_question(sheet_type: str):
    handler = SheetHandlerFactory.create_handler(sheet_type)
    result = process(handler)
    subject = handler.get_title(result["topic"])
    htmlContent = llm_service.generate_response(handler.get_title(result["topic"]))
    htmlContent = extract_html(htmlContent).strip()
    response = await send_email_request(subject, htmlContent)

    return result


@app.get("/daily_questions/{sheet_type}")
async def daily_questions(sheet_type: str):
    try:
        handler = SheetHandlerFactory.create_handler(sheet_type)
        result = []
        for _ in range(5):
            result.append(process(handler))
        return result
    except Exception as e:
        logger.exception(e)
        return {"error": "An error occurred", "message": str(e)}


def generate_htmlContent(topics, handler: SheetHandler) -> str:
    htmlContent = "<html><head><style>p { margin-top:0; } h2{margin-bottom:0;}</style></head><body>"
    for topic in topics:
        title = handler.get_title(topic["topic"])
        htmlContent += f"<h2>{title}</h2>"
        link = f"https://www.google.com/search?q={title}"
        link = handler.create_link(title)
        htmlContent += f"<p><a href={link}>Search on Google</a></p>"

    htmlContent += "</body></html>"
    return htmlContent


# email daily questions
@app.get("/email_daily_bites/{sheet_type}")
async def email_daily_questions(sheet_type: str):
    try:
        handler = SheetHandlerFactory.create_handler(sheet_type)
        result = []
        for _ in range(5):
            result.append(process(handler))
        subject = "Daily Bites"
        htmlContent = generate_htmlContent(result, handler)
        response = await send_email_request(subject, htmlContent)
        return result
    except Exception as e:
        logger.exception(e)
        return {"error": "An error occurred", "message": str(e)}
