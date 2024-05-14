@echo off
c:\masm32\bin\ml /c /Zd /coff amount_letter.asm
c:\\masm32\bin\Link /SUBSYSTEM:CONSOLE amount_letter.obj
pause
