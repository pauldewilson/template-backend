@REM activate the virtual environment at ./venv/Scripts/activate
@echo off

@REM Set the path to the virtual environment
set VIRTUAL_ENV=./venv/Scripts/activate

@REM Activate the virtual environment
call %VIRTUAL_ENV%

@REM Start the backend server
uvicorn app.main:app --port 5000 --host 0.0.0.0 --reload