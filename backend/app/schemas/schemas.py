from datetime import date, time
from pydantic import BaseModel, EmailStr
from app.models.models import UserRole, BookingStatus, PaymentStatus


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str | None = None
    role: UserRole = UserRole.customer


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole

    class Config:
        from_attributes = True


class BeauticianCreate(BaseModel):
    experience: int
    certifications: str
    location: str


class ServiceCreate(BaseModel):
    service_name: str
    price: float
    duration: int


class BookingCreate(BaseModel):
    beautician_id: int
    service_id: int
    date: date
    time: time


class BookingOut(BaseModel):
    id: int
    status: BookingStatus
    payment_status: PaymentStatus

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    beautician_id: int
    rating: int
    comment: str


class PaymentRequest(BaseModel):
    booking_id: int
    amount: float


class AIMakeupRequest(BaseModel):
    image_url: str


class AIMakeupResponse(BaseModel):
    style_previews: dict[str, str]
    suggested_specialists: list[dict]
