from pydantic import BaseModel
from typing import Optional, List

class Product(BaseModel):
    name: str
    price: int
    tags: Optional[List[str]]

    @property
    def as_dict(self):
        return {
            'msg': 'some message',
            'name': self.name,
            'price': self.price,
            'tags': self.tags
        }

class Buyer(BaseModel):
    id: int
    adres: str

class Cart(BaseModel):
    buyer: Buyer
    products: List[Product]