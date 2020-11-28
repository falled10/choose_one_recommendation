#!/usr/bin/env bash
#!/bin/sh


apt-get update && apt-get install -y netcat

echo "Waiting for neo4j..."

while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
  sleep 0.1
done

echo "Neoj4 started"

poetry run celery -A core worker -l INFO

exec "$@"
