@echo off
c:\masm32\bin\ml /c /Zd /coff main.asm
c:\\masm32\bin\Link /SUBSYSTEM:CONSOLE main.obj
pause
