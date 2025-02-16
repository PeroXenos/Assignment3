from fastapi import APIRouter, HTTPException
from app.db import db
from app.models import Order

router = APIRouter()

@router.post("/")
def create_order(order: Order):
    if not db.users.find_one({"_id": order.user_id}):
        raise HTTPException(status_code=404, detail="User not found")
    
    for item in order.products:
        product = db.products.find_one({"_id": item.product_id})
        if not product or product["stock"] < item.quantity:
            raise HTTPException(status_code=400, detail=f"Product {item.product_id} not available")
    
    db.orders.insert_one(order.dict())
    return {"message": "Order created successfully"}

@router.get("/{user_id}")
def get_orders(user_id: str):
    return list(db.orders.find({"user_id": user_id}, {"_id": 0}))
