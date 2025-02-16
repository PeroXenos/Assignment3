from fastapi import APIRouter
from app.routes import product_routes, user_routes, order_routes

router = APIRouter()

router.include_router(product_routes.router, prefix="/products", tags=["Products"])
router.include_router(user_routes.router, prefix="/users", tags=["Users"])
router.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
