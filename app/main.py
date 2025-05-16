from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.presentation.routers import auth
from app.domain.user import Base
from app.infrastructure.database import engine
from app.core.middleware import APIKeyMiddleware

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Authentication Demo",
    description="A simple authentication system with FastAPI",
    version="1.0.0"
)

# Add API Key middleware
app.add_middleware(APIKeyMiddleware)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with /api prefix
app.include_router(auth.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Authentication Demo"} 