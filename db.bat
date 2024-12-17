@echo off
REM Check if the --dropandcreate argument is passed
set DROP_AND_CREATE=false
for %%a in (%*) do (
    if "%%a"=="--dropandcreate" (
        set DROP_AND_CREATE=true
    )
)

REM Set variables
set PGPASSWORD=postgres
set PGUSER=postgres
set PGHOST=localhost
set DBNAME=template_backend
set SQLFILE=db.sql

REM Ensure psql is in the PATH or provide the full path to psql
set PSQL_CMD=psql -U %PGUSER% -h %PGHOST%

if "%DROP_AND_CREATE%"=="true" (
    REM Drop the database if it exists and create a new one
    echo Dropping and recreating the database...
    %PSQL_CMD% -c "DROP DATABASE IF EXISTS %DBNAME%;"
    %PSQL_CMD% -c "CREATE DATABASE %DBNAME%;"
) else (
    REM Check if the database exists
    echo Checking if the database exists...
    %PSQL_CMD% -tAc "SELECT 1 FROM pg_database WHERE datname='%DBNAME%';" | find "1" >nul
    if errorlevel 1 (
        echo Database does not exist. Creating it...
        %PSQL_CMD% -c "CREATE DATABASE %DBNAME%;"
    ) else (
        echo Database %DBNAME% already exists.
    )
)

REM Execute the db.sql file
if exist %SQLFILE% (
    echo Running SQL file %SQLFILE%...
    %PSQL_CMD% -d %DBNAME% -f %SQLFILE%
) else (
    echo SQL file %SQLFILE% not found!
)

REM Clear PGPASSWORD for security
set PGPASSWORD=
