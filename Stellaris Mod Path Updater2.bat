@echo off
REM Change the directory to the folder containing the Python script
cd "C:\path\to\your\python\script"

REM Try running with the default Python in the PATH
python --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Running with default Python installation...
    python SMPU.py
) ELSE (
    echo Default Python not found. Trying common Python installation paths...
    
    REM Fallback to common Python installation paths
    IF EXIST "C:\Python39\python.exe" (
        "C:\Python39\python.exe" SMPU.py
    ) ELSE IF EXIST "C:\Python38\python.exe" (
        "C:\Python38\python.exe" SMPU.py
    ) ELSE IF EXIST "C:\Program Files\Python39\python.exe" (
        "C:\Program Files\Python39\python.exe" SMPU.py
   
) ELSE (
    echo Default Python not found. Trying the hardcoded Python path...
    
    REM Fallback to the hardcoded path if default Python is not in PATH
    "C:\path\to\python\python.exe" SMPU.py
)

REM Keep the window open so users can see the output
pause
