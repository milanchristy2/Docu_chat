from fastapi import APIRouter

from backend.src.app.api.routes.chat_router import router as chat_router
from backend.src.app.api.routes.query_router import router as query_router
from backend.src.app.api.routes.upload_router import router as upload_router

router=APIRouter()

router.include_router(chat_router)
router.include_router(query_router)
router.include_router(upload_router)