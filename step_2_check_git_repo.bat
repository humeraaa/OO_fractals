@echo off
SETLOCAL

echo =====================================
echo STEP 2: Check if Git Repo is Initialized
echo =====================================
echo.

rem Display current directory
echo Current working directory:
cd
echo.

rem Check if .git folder exists
IF NOT EXIST ".git" (
    echo  This folder is NOT a Git repository.
    echo You can initialize one using:
    echo   git init
    pause
    exit /b
) ELSE (
    echo  This folder IS a Git repository.
)

echo.
pause
