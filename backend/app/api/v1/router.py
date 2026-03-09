from fastapi import APIRouter
from app.api.v1.endpoints import auth, beauticians, bookings, reviews, payments, ai, admin

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(beauticians.router)
api_router.include_router(bookings.router)
api_router.include_router(reviews.router)
api_router.include_router(payments.router)
api_router.include_router(ai.router)
api_router.include_router(admin.router)
