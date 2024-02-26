#!/bin/bash

# Made by Nick Kipshidze

if [ -z "$1" ]; then
    echo "[start] Please provide an argument"
    exit 1
fi

if [ "$1" = "backend" ]; then
    echo "[start] Starting backend server"
    cd ./backend
    python3 manage.py migrate
    python3 manage.py runserver localhost:8000
elif [ "$1" = "frontend" ]; then
    echo "[start] Starting frontend server"
    cd ./frontend
    npm run dev
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
