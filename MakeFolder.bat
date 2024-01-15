@echo off
set /p folderStructure=Enter the folder structure (e.g., Example/test/result):

mkdir "%folderStructure%"

echo Folders created successfully!
pause
