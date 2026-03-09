from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.models import Booking, Payment, PaymentStatus
from app.schemas.schemas import PaymentRequest
from app.services.payment_service import RazorpayService

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("/create-order")
def create_order(payload: PaymentRequest, user=Depends(get_current_user), db: Session = Depends(get_db)):
    booking = db.get(Booking, payload.booking_id)
    if not booking or booking.customer_id != user.id:
        raise HTTPException(status_code=404, detail="Booking not found")

    service = RazorpayService()
    order = service.create_order(payload.amount)

    payment = Payment(
        booking_id=payload.booking_id,
        amount=payload.amount,
        status=PaymentStatus.pending,
        razorpay_order_id=order.get("id"),
    )
    db.add(payment)
    db.commit()
    return {"order": order}
