@echo off
SETLOCAL

echo ============================================
echo STEP 3: Check and Add Git Remote 'origin'
echo ============================================
echo.

rem Navigate to the actual project folder (edit project_dir if needed)
set "project_dir=OO_frctals"
cd /d "%~dp0%project_dir%"

rem Check if Git remote 'origin' is set
git remote get-url origin >nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo   Remote 'origin' not found. Attempting to add...
    git remote add origin https://github.com/humeraaa/OO_frctals.git
    IF %ERRORLEVEL% EQU 0 (
        echo  Remote 'origin' successfully added.
    ) ELSE (
        echo  Failed to add remote 'origin'. Please check the URL or permissions.
        pause
        exit /b
    )
) ELSE (
    echo  Remote 'origin' already exists.
)

echo.
echo Current Git remotes:
git remote -v

echo.
pause
