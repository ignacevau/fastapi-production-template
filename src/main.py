from fastapi import FastAPI

from src.config import settings
from src.database import db
from src.user.router import user


def init_app():
    db.init()

    APP_CONFIG = {
        "title": "FastAPI Template",
        "description": "Description of this FastAPI server.",
    }

    if settings.ENVIRONMENT == "production":
        APP_CONFIG["openapi_url"] = None

    app = FastAPI(**APP_CONFIG)

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    app.include_router(
        user,
        prefix="/api/v1",
    )

    return app


app = init_app()
