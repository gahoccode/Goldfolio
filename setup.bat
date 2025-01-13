@echo off
setlocal enabledelayedexpansion

:: Setup script for Python project environment management
set "VENV_DIR=venv"
set "REQUIREMENTS_FILE=requirements.txt"
set "MAIN_APP=st.py"

:: Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

:: Create virtual environment if it doesn't exist
if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
) else (
    echo Virtual environment already exists
)

:: Activate virtual environment
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

:menu
cls
echo ================================
echo        Goldfolio Setup
echo ================================
echo.
echo Virtual Environment Status: Active
echo Current Python: !VIRTUAL_ENV!
echo.
echo Available Options:
echo 1. Install Dependencies
echo 2. Update Dependencies
echo 3. Run Application
echo 4. Exit
echo.
set /p CHOICE="Enter your choice (1-4): "

if "%CHOICE%"=="1" (
    echo Installing dependencies...
    pip install -r "%REQUIREMENTS_FILE%"
    if errorlevel 1 (
        echo Error: Failed to install dependencies
    ) else (
        echo Dependencies installed successfully
    )
    pause
    goto menu
)

if "%CHOICE%"=="2" (
    echo Updating dependencies...
    pip install --upgrade -r "%REQUIREMENTS_FILE%"
    if errorlevel 1 (
        echo Error: Failed to update dependencies
    ) else (
        echo Dependencies updated successfully
    )
    pause
    goto menu
)

if "%CHOICE%"=="3" (
    echo Starting application...
    streamlit run "%MAIN_APP%"
    if errorlevel 1 (
        echo Error: Application failed to start
    )
    pause
    goto menu
)

if "%CHOICE%"=="4" (
    echo Exiting...
    exit /b 0
)

echo Invalid choice. Please try again.
pause
goto menu
