from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Product(BaseModel):
    name: str
    price: float
    description: str
    category: str
    stock: int

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "customer"

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    user_id: str
    products: List[OrderItem]
    status: str = "pending"
