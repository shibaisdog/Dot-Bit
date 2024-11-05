call "%~dp0/venv/Scripts/activate.bat"
pyinstaller --noconsole --onefile --name=Dot-Bit ./env/display.py
call "%~dp0/venv/Scripts/deactivate.bat"
pause