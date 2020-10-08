@echo off
:a
python "C:\Users\user\Documents\Web\www\Site\Site\__init__.py"
echo retrying in 2 seconds
timeout /t 2>nul
goto a
@echo on