from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.models import UserRole, Beautician, User, Booking

router = APIRouter(prefix="/admin", tags=["admin"])


def admin_guard(user):
    if user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Admin only")


@router.patch("/beauticians/{beautician_id}/verify")
def verify_beautician(beautician_id: int, verified: bool, user=Depends(get_current_user), db: Session = Depends(get_db)):
    admin_guard(user)
    profile = db.get(Beautician, beautician_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Beautician not found")
    profile.is_verified = verified
    db.commit()
    return {"message": "Updated"}


@router.get("/overview")
def overview(user=Depends(get_current_user), db: Session = Depends(get_db)):
    admin_guard(user)
    return {
        "users": db.query(User).count(),
        "beauticians": db.query(Beautician).count(),
        "bookings": db.query(Booking).count(),
    }
