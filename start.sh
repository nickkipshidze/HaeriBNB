#!/bin/bash

# Made by Nick Kipshidze

if [ -z "$1" ]; then
    echo "[start] Please provide an argument"
    exit 1
fi

check_python() {
    echo "[start] Checking python..."
    if command -v python3 &>/dev/null; then
        echo "[start] Python3 is installed - version: $(python3 --version)"
    else
        echo "[start] Python3 is not installed"
        exit 1
    fi
}

check_npm() {
    echo "[start] Checking npm..."
    if command -v npm &>/dev/null; then
        echo "[start] npm is installed - version: $(npm --version)"
    else
        echo "[start] npm is not installed"
        exit 1
    fi
}

if [ "$1" = "backend" ]; then
    check_python

    cd ./backend

    if [ "$2" = "makemigrations" ]; then
        echo "[start] Making migrations..."
        python3 manage.py makemigrations
    
    elif [ "$2" = "migrate" ]; then
        echo "[start] Migrating database..."
        python3 manage.py migrate
    
    elif [ "$2" = "mksudo" ]; then
        python3 manage.py createsuperuser

    else
        echo "[start] Starting backend server"
        python3 manage.py runserver localhost:8000
    fi

elif [ "$1" = "frontend" ]; then
    check_npm

    echo "[start] Starting frontend server"

    cd ./frontend
    npm run dev

elif [ "$1" = "install" ]; then
    check_python
    check_npm

    echo "[start] Installing python dependencies..."
    cd ./backend
    python3 -m pip install -r requirements.txt

    echo "[start] Installing npm dependencies..."
    cd ../frontend
    npm install

elif [ "$1" = "cleanup" ]; then
    echo "[start] Cleaning up..."

    find . -type d -name "__pycache__" -exec rm -r {} +
    rm -rf ./frontend/.next

elif [ "$1" = "count" ]; then
    echo "[start] Counting lines of code..."

    git ls-files -- "*.py" "*.js" "*.css" "*.txt" "*.md" "*.sh" | xargs wc -l

else
    echo "[start] Invalid argument: $1"
    exit 1
fi
