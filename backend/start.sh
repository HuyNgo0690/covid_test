#!/bin/bash
#exec flask db init &
#exec flask db migrate &
#exec flask db upgrade &
#exec python main.py
exec gunicorn main:backend --error-logfile="$GUNICORN_ERROR_LOG" --workers=6 --bind=0.0.0.0:3001 --timeout=120 &