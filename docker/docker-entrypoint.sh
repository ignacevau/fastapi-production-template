#!/bin/sh

set -e

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

# SETUP
# run alembic migrations
alembic upgrade head


# Evaluating passed command:
exec "$@"