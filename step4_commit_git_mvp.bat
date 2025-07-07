@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

echo ================================
echo Step 4: MVP Commit and Push to GitHub
echo ================================
echo.

:: Step 1: Ensure Git is installed
git --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Git is not installed or not available in PATH.
    pause
    exit /b
)

:: Step 2: Ensure current folder is a Git repository
IF NOT EXIST ".git" (
    echo This is not a Git repository. Please run git init and set remote first.
    pause
    exit /b
)

:: Step 3: Check if remote 'origin' is configured
git remote get-url origin >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Remote 'origin' not found.
    echo Use: git remote add origin https://github.com/humeraaa/chat-application.git
    pause
    exit /b
)

echo Remote 'origin' is set correctly.

:: Step 4: Configure Git identity
git config --global user.name "humeraaa"
git config --global user.email "humera@uok.edu.pk"

:: Step 5: Generate commit message
for /f %%A in ('powershell -Command "Get-Date -Format yyyy-MM-dd_HH-mm-ss"') do set datetime=%%A
set "msg=MVP Commit - %datetime%"

:: Step 6: Add all changes and commit
git add .

:: Skip commit if nothing changed
git diff --cached --quiet
IF %ERRORLEVEL% EQU 0 (
    echo Nothing to commit. Working tree clean.
) ELSE (
    echo Committing with message: %msg%
    git commit -m "%msg%"
)

:: Step 7: Try push
echo Pushing to GitHub...
git push origin main
IF %ERRORLEVEL% NEQ 0 (
    echo Push failed. Attempting to pull remote changes and retry...
    git pull origin main --allow-unrelated-histories
    echo Merging changes...
    git push origin main
)

:: Step 8: Done
echo.
echo Step 4 complete: Commit and push process finished.
pause
