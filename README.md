# DreamMakeovers MVP

Production-ready MVP scaffold for a beauty-service marketplace connecting customers and certified beauticians.

## Repository structure
- `backend/` FastAPI service (JWT auth, bookings, reviews, payments, AI preview)
- `frontend/` Next.js + Tailwind web app
- `mobile/` Expo React Native app
- `database/` PostgreSQL schema SQL
- `docker/` container orchestration
- `docs/` architecture and deployment docs

## Core implemented modules
### Backend APIs
- Auth: register/login with JWT
- Beauticians: profile + services + search
- Bookings: create/update/list
- Reviews: create + rating aggregation
- Payments: Razorpay order creation placeholder
- AI Makeup Preview: style previews + specialist suggestions placeholder
- Admin: beautician verification + platform overview

### Frontend pages
- Home
- Search beauticians
- Beautician profile page
- Booking page
- User dashboard

### Mobile screens
- Login/Signup
- Browse beauticians
- Booking
- Payment
- Profile

## Run locally with Docker
```bash
cd docker
docker compose up --build
```

## Backend local run
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment variables (backend)
- `SECRET_KEY`
- `DATABASE_URL`
- `RAZORPAY_KEY_ID`
- `RAZORPAY_KEY_SECRET`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_S3_BUCKET`

## Future production hardening
- OAuth providers and refresh-token rotation
- Celery/RQ workers for async jobs
- Redis cache and rate limiting
- Full observability stack
- CI/CD pipeline and IaC (Terraform)
