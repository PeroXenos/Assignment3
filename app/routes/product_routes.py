from fastapi import APIRouter, HTTPException
from app.db import db
from app.models import Product

router = APIRouter()

@router.post("/")
def create_product(product: Product):
    if db.products.find_one({"name": product.name}):
        raise HTTPException(status_code=400, detail="Product already exists")
    db.products.insert_one(product.dict())
    return {"message": "Product added successfully"}

@router.get("/")
def get_products():
    return list(db.products.find({}, {"_id": 0}))

@router.delete("/{name}")
def delete_product(name: str):
    result = db.products.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}
