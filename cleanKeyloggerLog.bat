@echo off
setlocal enabledelayedexpansion

set "logFolder=%~dp0keyloggerLog"

if not exist "!logFolder!" (
    echo Folder does not exist.
    exit /b
)

for /f "delims=" %%f in ('dir /b /a-d "%logFolder%\*"') do (
    echo Deleting file: %%f
    del /q "%logFolder%\%%f"
)

rmdir /s /q "%logFolder%"

echo Complete.
endlocal