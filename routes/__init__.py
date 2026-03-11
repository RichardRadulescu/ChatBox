from .fileRoutes import router as file_router
from .userRoutes import router as user_router
from .auth.auth import router as auth_router

# This tells Python what is "public" when someone imports * from the package
__all__ = ["file_router", "user_router", "auth_router"]

