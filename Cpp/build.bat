@echo off
if not exist sqlite3.o (
    echo Compiling sqlite3.c...
    gcc -c sqlite3.c -o sqlite3.o
)
echo Compiling and linking...
g++ -g Library_Manager.cpp sqlite3.o -o Library_Manager.exe
if %errorlevel% neq 0 (
    echo Build Failed!
    pause
    exit /b %errorlevel%
)
echo Build Successful!
Library_Manager.exe
pause