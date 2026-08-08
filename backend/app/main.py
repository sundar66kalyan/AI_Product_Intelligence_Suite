from app.modules.ai.routers.moodboard_router import router as moodboard_router
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.core.logger import logger
from app.database.init_db import create_tables
from app.api.v1.products import router as product_router
from app.modules.market.routers.trend_router import router as trend_router
from app.modules.ai.routers.market_ai_router import router as ai_router
from app.modules.product_intelligence.routers.product_router import router as product_ai_router
from app.api import history
from app.modules.market.routers.dashboard_router import router as dashboard_router
from app.modules.ai.routers.insights_router import router as insights_router
from app.api import gemini_report
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    logger.info("Database initialized successfully.")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, tags=["Health"])
app.include_router(product_router)
app.include_router(trend_router)
app.include_router(ai_router)
app.include_router(product_ai_router)
app.include_router(history.router)
app.include_router(dashboard_router)
app.include_router(insights_router)
app.include_router(moodboard_router)
app.include_router(gemini_report.router)
@app.get("/", tags=["Root"])
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running"
    }


logger.info("Application Started Successfully")