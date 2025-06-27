#!/bin/bash

set -e  # Exit immediately on error

#Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

echo "Docker is installed. Continuing with build..."

# --- Config ---
REPO_URL="https://github.com/jason-erasmus/web-service.git"
CLONE_DIR="app-temp"

echo "Cloning the repository..."
rm -rf $CLONE_DIR
git clone $REPO_URL $CLONE_DIR
cd $CLONE_DIR

echo "Building Docker image..."
docker compose build

echo "Running Django migrations..."
docker compose run django python manage.py migrate


echo "Starting application..."
docker compose up -d

echo "Done! Visit http://localhost:3000"

