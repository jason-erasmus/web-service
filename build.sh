#!/bin/bash

set -e  # Exit immediately on error

# --- Config ---
REPO_URL="https://github.com/jason-erasmus/web-service.git"
CLONE_DIR="app-temp"

echo "📥 Cloning the repository..."
rm -rf $CLONE_DIR
git clone $REPO_URL $CLONE_DIR
cd $CLONE_DIR

echo "🐳 Building Docker image..."
docker compose build

echo "🗃️ Running Django migrations..."
docker compose run server python manage.py migrate

# Optional: Create superuser
# echo "👤 Creating Django superuser..."
# docker compose run server python manage.py createsuperuser

echo "🟢 Starting application..."
docker compose up -d

echo "✅ Done! Visit http://localhost:8000"
