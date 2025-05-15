from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.core.middleware import APIKeyMiddleware
from app.presentation.api.auth_routes import router as auth_router
from app.presentation.api.user_routes import create_user_routes
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.application.services.user_service import UserService

# Create database tables
Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    app = FastAPI()
    
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add API key middleware
    app.add_middleware(APIKeyMiddleware)
 
    # Dependency injection
    # user_repository = UserRepositoryImpl()
    user_service = UserService(user_repository)

    # Include routers
    # app.include_router(auth_router, prefix="/auth", tags=["authentication"])
    app.include_router(create_user_routes(user_service), prefix="/api", tags=["users"])

    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    return app

app = create_app()