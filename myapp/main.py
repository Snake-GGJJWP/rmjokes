from fastapi import FastAPI, Query, Path
from typing import List, Optional

from .models import Cart, Product

import uvicorn

app = FastAPI()

@app.post('/add_items/{buyer_id}')
def add_items(*, buyer_id: int, items: List[Product]):
    if not buyer_id:
        return {'detail': '''you can't enter empty id'''}
    response = {'items_added': [item for item in items if item.price>100]}
    return response

@app.get('/show_cart/{buyer_id}')
def show_cart(*, buyer_id: int = Path(default = None, gt=0), cart: Cart):
    if not buyer_id:
        return {'detail': '''you can't enter empty id'''}
    return cart

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)