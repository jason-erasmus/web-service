# build.ps1
$ErrorActionPreference = "Stop"  # Exit on any error

# --- Config ---
$REPO_URL = "https://github.com/jason-erasmus/web-service.git"
$CLONE_DIR = "app-temp"

Write-Host "Cloning the repository..."
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue $CLONE_DIR
git clone $REPO_URL $CLONE_DIR
Set-Location $CLONE_DIR

Write-Host "Building Docker image..."
docker compose build

Write-Host "Running Django migrations..."
docker compose run django python manage.py migrate


Write-Host "Starting application..."
docker compose up -d

Write-Host "Done! Visit http://localhost:3000"
