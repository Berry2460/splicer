@echo off
python -m pip install --upgrade pip
pip install pyinstaller
pyinstaller -F "OOF-Splicer.py"
pyinstaller -F "OOF-Stitcher.py"
pause
