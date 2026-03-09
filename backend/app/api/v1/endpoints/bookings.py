from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.models import Booking, Service, UserRole, Beautician, BookingStatus
from app.schemas.schemas import BookingCreate, BookingOut

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("/", response_model=BookingOut)
def create_booking(payload: BookingCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user.role != UserRole.customer:
        raise HTTPException(status_code=403, detail="Only customers can create bookings")
    service = db.get(Service, payload.service_id)
    if not service or service.beautician_id != payload.beautician_id:
        raise HTTPException(status_code=404, detail="Service not found")

    booking = Booking(customer_id=user.id, **payload.model_dump())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


@router.patch("/{booking_id}/status")
def update_status(booking_id: int, status: BookingStatus, user=Depends(get_current_user), db: Session = Depends(get_db)):
    booking = db.get(Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    beautician = db.query(Beautician).filter(Beautician.id == booking.beautician_id, Beautician.user_id == user.id).first()
    if not beautician and user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Unauthorized")
    booking.status = status
    db.commit()
    return {"message": "Booking updated"}


@router.get("/me")
def my_bookings(user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user.role == UserRole.customer:
        return db.query(Booking).filter(Booking.customer_id == user.id).all()
    if user.role == UserRole.beautician:
        beautician = db.query(Beautician).filter(Beautician.user_id == user.id).first()
        if not beautician:
            return []
        return db.query(Booking).filter(Booking.beautician_id == beautician.id).all()
    return db.query(Booking).all()
