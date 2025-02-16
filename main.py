from fastapi import FastAPI, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from bson import ObjectId
import os

# Настройки MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "ecommerce"

app = FastAPI()
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Модели данных
class Product(BaseModel):
    name: str
    price: float
    description: str
    category: str
    stock: int

class User(BaseModel):
    name: str
    email: str
    password: str
    role: str

class Order(BaseModel):
    user_id: str
    product_ids: list[str]
    order_status: str

# CRUD для продуктов
@app.post("/products/")
async def create_product(product: Product):
    new_product = await db.products.insert_one(product.dict())
    return {"id": str(new_product.inserted_id)}

@app.get("/products/{product_id}")
async def get_product(product_id: str):
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if product:
        product["id"] = str(product["_id"])
        del product["_id"]
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}")
async def update_product(product_id: str, product: Product):
    updated = await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product.dict()})
    if updated.modified_count:
        return {"message": "Product updated"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    deleted = await db.products.delete_one({"_id": ObjectId(product_id)})
    if deleted.deleted_count:
        return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")