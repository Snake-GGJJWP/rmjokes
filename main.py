from fastapi import FastAPI
app = FastAPI()
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int

@app.post('/{item_id}')
async def root(item_id: str, item: Item):
    return {'name': item.name, 'price': item.price}