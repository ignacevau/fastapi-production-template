setlocal
@REM load env variables
FOR /F "eol=# tokens=*" %%i IN (dev.host.env) DO SET %%i

@REM run alembic
poetry run alembic downgrade base
endlocal