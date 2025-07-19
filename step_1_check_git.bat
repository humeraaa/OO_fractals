@echo off
SETLOCAL

echo ===================================
echo STEP 1: Basic Git Environment Check
echo ===================================
echo.

rem Display current directory
echo Current working directory:
cd
echo.

rem Check if Git is installed
git --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Git is NOT installed or not added to PATH.
    echo Please install Git from: https://git-scm.com/downloads
    pause
    exit /b
) ELSE (
    echo Git is installed and available in PATH.
)

echo.
echo  Git environment check passed.
pause

