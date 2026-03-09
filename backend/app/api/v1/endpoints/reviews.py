from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.models import Review, UserRole, Beautician
from app.schemas.schemas import ReviewCreate

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/")
def create_review(payload: ReviewCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user.role != UserRole.customer:
        raise HTTPException(status_code=403, detail="Only customers can post reviews")
    review = Review(customer_id=user.id, **payload.model_dump())
    db.add(review)
    db.commit()

    avg = db.query(func.avg(Review.rating)).filter(Review.beautician_id == payload.beautician_id).scalar() or 0
    profile = db.query(Beautician).filter(Beautician.id == payload.beautician_id).first()
    if profile:
        profile.rating = round(float(avg), 2)
        db.commit()
    return {"message": "Review added"}
