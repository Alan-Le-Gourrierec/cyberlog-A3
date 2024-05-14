@echo off
c:\masm32\bin\ml /c /Zd /coff conversion.asm
c:\\masm32\bin\Link /SUBSYSTEM:CONSOLE conversion.obj
pause
