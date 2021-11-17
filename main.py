from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Product(BaseModel):
    name: str
    price: int
    tags: Optional[list[str]]

    @property
    def as_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'tags': self.tags
        }


@app.post('/add_item/')
def add_item(product: Product):
    return product.as_dict