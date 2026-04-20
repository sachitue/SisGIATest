@echo off
cd /d D:\CollegeManagement-Django
call venv\Scripts\activate.bat
python import_students_from_excel.py
pause