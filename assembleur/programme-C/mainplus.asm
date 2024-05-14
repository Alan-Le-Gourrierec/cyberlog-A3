.386
.model flat,stdcall
option casemap:none

include c:\masm32\include\windows.inc
include c:\masm32\include\gdi32.inc
include c:\masm32\include\gdiplus.inc
include c:\masm32\include\user32.inc
include c:\masm32\include\kernel32.inc
include c:\masm32\include\msvcrt.inc

includelib c:\masm32\lib\gdi32.lib
includelib c:\masm32\lib\kernel32.lib
includelib c:\masm32\lib\user32.lib
includelib c:\masm32\lib\msvcrt.lib

.DATA
	;n dword 10
	result db "resutat = %d",0
	input db "%d",0

.DATA?

.CODE
	fibonachi PROC
		;debut de la fonction
		push ebp
		mov ebp, esp

		pushad 

		;varriable locales
		mov ecx, [ebp+8]; n
		add ecx, 1	
		; initialisation
		mov eax, 1; j
		mov ebx, 1; k

		mov esi, 3; i = 3
		jmp loop_func

	loop_func:
		mov edx, eax; l = j
		add edx, ebx; l = l + k
		mov eax, ebx; j = k
		mov ebx, edx; k = l

		inc esi; i++
	
	loop_fin:
		cmp esi, ecx; comparaison enx et ecx	
		jle loop_func; si i <= n jmp à loop

		push eax
		push offset result
		call crt_printf
		add esp,8

		popad
		pop ebp
		ret

	fibonachi ENDP

	start:
		push offset n
		call fibonachi

		push 0
		call ExitProcess
	end start
