#!/usr/bin/env bash

# Check for existing migrations, excluding "Initial Migration"
if alembic current | grep -q -v "Initial Migration"; then
    echo "Existing Initial migration found. Skipping initial migration."
else
    # Generate initial migration if no migration has been done
    alembic revision --autogenerate -m "Initial Migration"
    sleep 10  # Optional delay for database operations
    alembic upgrade head
fi

celery -A tasks worker -l info &
celery -A tasks beat -l info &

# Start the app
exec "$@"
