# Deployment Guide (AWS EC2)

1. Provision Ubuntu EC2 instance and install Docker + Docker Compose.
2. Clone repository and configure environment files.
3. Start stack:
   ```bash
   cd docker
   docker compose up --build -d
   ```
4. Configure reverse proxy (Nginx) for TLS and domain routing:
   - `api.yourdomain.com -> backend:8000`
   - `app.yourdomain.com -> frontend:3000`
5. Set production env vars for JWT secret, Razorpay keys, S3 credentials.
6. Attach CloudWatch/Prometheus for health and metrics.
