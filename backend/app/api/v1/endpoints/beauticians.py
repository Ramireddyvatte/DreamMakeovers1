from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.models import Beautician, Service, UserRole
from app.schemas.schemas import BeauticianCreate, ServiceCreate

router = APIRouter(prefix="/beauticians", tags=["beauticians"])


@router.post("/profile")
def create_profile(payload: BeauticianCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user.role != UserRole.beautician:
        raise HTTPException(status_code=403, detail="Only beauticians can create profile")
    profile = Beautician(user_id=user.id, **payload.model_dump())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


@router.post("/{beautician_id}/services")
def add_service(beautician_id: int, payload: ServiceCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    profile = db.query(Beautician).filter(Beautician.id == beautician_id, Beautician.user_id == user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Beautician profile not found")
    service = Service(beautician_id=beautician_id, **payload.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.get("/search")
def search_beauticians(location: str = "", min_price: float = 0, max_price: float = 100000, db: Session = Depends(get_db)):
    return (
        db.query(Beautician, Service)
        .join(Service, Service.beautician_id == Beautician.id)
        .filter(Beautician.location.ilike(f"%{location}%"))
        .filter(Service.price.between(min_price, max_price))
        .all()
    )
