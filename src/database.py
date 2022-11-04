from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr
from sqlalchemy import MetaData
from fastapi.encoders import jsonable_encoder

from src.config import settings


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}


@as_declarative()
class Base():
    __name__: str

    def serializable_dict(self, **kwargs):
        """Return a dict which contains only serializable fields."""
        default_dict = super().dict(**kwargs)

        return jsonable_encoder(default_dict)

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self._session, name)

    def init(self):
        self._engine = create_async_engine(
            settings.DATABASE_URL,
            future=True,
            echo=True,
        )
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()


db = AsyncDatabaseSession()
metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)