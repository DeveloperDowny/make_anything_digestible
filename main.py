from fastapi import FastAPI
from pydantic import BaseModel

from random_striver_sheet_question_opener.v2 import SheetHandlerFactory

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

@app.get("/random_question/{sheet_type}")
async def random_question(sheet_type: str):
    handler = SheetHandlerFactory.create_handler(sheet_type)
    # handler.process() 
    # catch whatever the above command prints
    # and return it as a response
    return {"message": "Question processed successfully."}
     