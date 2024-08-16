from fastapi import FastAPI
from pydantic import BaseModel

from random_striver_sheet_question_opener.v2 import SheetHandlerFactory

import json
import logging

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_active: bool


@app.post("/items/")
async def create_item(item: Item):
    # Process the received item
    # Save it to the database or perform any other operations

    # Return the processed item
    return item


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # Retrieve the item from the database using the item_id

    # Return the retrieved item
    return {"item_id": item_id}


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
