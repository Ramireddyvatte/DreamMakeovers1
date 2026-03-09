import enum
from datetime import datetime, date, time
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, Date, Time, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base


class UserRole(str, enum.Enum):
    customer = "customer"
    beautician = "beautician"
    admin = "admin"


class BookingStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    completed = "completed"


class PaymentStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20))
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.customer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Beautician(Base):
    __tablename__ = "beauticians"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    experience: Mapped[int] = mapped_column(Integer, default=0)
    certifications: Mapped[str] = mapped_column(Text, default="[]")
    location: Mapped[str] = mapped_column(String(255), default="")
    rating: Mapped[float] = mapped_column(Float, default=0.0)
    is_verified: Mapped[bool] = mapped_column(default=False)

    user: Mapped["User"] = relationship()


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    beautician_id: Mapped[int] = mapped_column(ForeignKey("beauticians.id"))
    service_name: Mapped[str] = mapped_column(String(120), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    beautician_id: Mapped[int] = mapped_column(ForeignKey("beauticians.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    date: Mapped[date] = mapped_column(Date)
    time: Mapped[time] = mapped_column(Time)
    status: Mapped[BookingStatus] = mapped_column(Enum(BookingStatus), default=BookingStatus.pending)
    payment_status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.pending)


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    beautician_id: Mapped[int] = mapped_column(ForeignKey("beauticians.id"))
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(Text)


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.id"))
    amount: Mapped[float] = mapped_column(Float)
    payment_method: Mapped[str] = mapped_column(String(50), default="razorpay")
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.pending)
    razorpay_order_id: Mapped[str | None] = mapped_column(String(120))
