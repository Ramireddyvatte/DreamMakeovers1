from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.models import Beautician, Service
from app.schemas.schemas import AIMakeupRequest, AIMakeupResponse
from app.services.ai_makeup import generate_makeup_preview

router = APIRouter(prefix="/ai", tags=["ai makeup preview"])


@router.post("/makeup-preview", response_model=AIMakeupResponse)
def makeup_preview(payload: AIMakeupRequest, db: Session = Depends(get_db)):
    preview = generate_makeup_preview(payload.image_url)
    suggestions = (
        db.query(Beautician.id, Beautician.location, Beautician.rating, Service.service_name)
        .join(Service, Service.beautician_id == Beautician.id)
        .filter(Service.service_name.ilike("%makeup%"))
        .limit(5)
        .all()
    )
    return {
        "style_previews": preview["style_previews"],
        "suggested_specialists": [
            {
                "beautician_id": s.id,
                "location": s.location,
                "rating": s.rating,
                "speciality": s.service_name,
            }
            for s in suggestions
        ],
    }
