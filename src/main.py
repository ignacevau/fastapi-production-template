from fastapi import FastAPI

from src.database import db
from src.views import api


def init_app():
    db.init()

    APP_CONFIG = {
        "title": "FastAPI Template",
        "description": "Description of this FastAPI server."
    }

    app = FastAPI(**APP_CONFIG)

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()


    app.include_router(
        api,
        prefix="/api/v1",
    )

    return app


app = init_app()
