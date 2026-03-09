# DreamMakeovers MVP Architecture

## High-level design
- **Frontend (Next.js)**: customer discovery, booking flows, dashboards.
- **Mobile (Expo React Native)**: customer booking and profile management.
- **Backend (FastAPI)**: auth, beautician, booking, payment, AI-preview APIs.
- **PostgreSQL**: transactional source of truth.
- **AWS S3**: image/document storage (portfolio + certificates).
- **Razorpay**: payment order + capture.
- **Google Maps**: location search and distance sort.
- **WebSocket channel**: real-time booking status updates.

## Scalability notes
- Stateless API instances behind load balancer.
- DB indexing for location, price, booking date.
- Background workers for heavy tasks (image processing, payout reconciliation).
- Caching search results (Redis recommended in phase 2).
- S3 pre-signed uploads reduce API file traffic.
