#!/bin/sh

echo "Waiting for fastapi..."

uvicorn main:app --host 0.0.0.0 --port 5001 --reload


echo "Fastapi started"


exec "$@"