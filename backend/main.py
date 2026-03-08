# backend/main.py

from fastapi import FastAPI
from backend.api.notices import router as notices_router

# We create a FastAPI "app" — this is the core of our API server
app = FastAPI(
    title="Academic Notification Engine",
    description="An intelligent system for parsing and prioritizing academic notices",
    version="0.1.0"
)
app.include_router(notices_router)

# A simple health check route — always good practice
# When someone visits /health, they get a confirmation the server is alive
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is running"}