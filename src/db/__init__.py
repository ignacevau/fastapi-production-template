# isort: skip_file

# this is only to allow autogenerate for alembic
# alembic uses db._Base, user models use db.base.Base
from .base import Base as _Base
from src.models import *
