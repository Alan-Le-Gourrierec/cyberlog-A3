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
	result db "nombre de a = %d, nombre de b = %d, nombre de c = %d",0
	mot db "abcabschascabciahbciabciabciabciabchbzhubaibcaiubcihabcugedbcabhuabcyhubegbec6ecbebcuyebuycvgbreuh8huhertjoubbbbbbbbbcdfzydugydutfcaaaaacaahregiejrgohrtigjraertyuiovdcdbvrfefbgejfguqyfyueqdbfvckjnvbiuerjfnv efogrtfblisrtghroigherfjhausgdchxqjhh",0

.DATA?

.CODE
	letter PROC
		;debut de la fonction
		push ebp
		mov ebp, esp
		pushad 	;initialiser les registres

		; initialisation
		mov eax, 0; pointeur vers les address

		mov DWORD PTR [ebp-4],0; nombre de a
		mov DWORD PTR [ebp-8],0; nombre de b
		mov DWORD PTR [ebp-12],0; nombre de c

		mov esi, 0; clear esi

		mov esi, [ebp + 8]; 
		jmp loop_function

	loop_function:
		mov al, [esi] 
		or al, al; fin?
		jz loop_end

		cmp al,'a'
		je count_a
		cmp al, 'b'
		je count_b
		cmp al, 'c'
		je count_c

		inc esi
		jmp loop_function
	loop_end:
		popad; clear registre 
		mov eax, [ebp-4] ; nbr a => eax
		mov ebx, [ebp-8] ; nbr b => ebx
		mov ecx, [ebp-12] ; nbr c => ecx

		pop ebp
		ret ; return

	count_a:
		mov eax,[ebp-4]
		inc eax
		mov [ebp-4], eax
		inc esi
		jmp loop_function
	
	count_b:
		mov ebx,[ebp-8]
		inc ebx
		mov [ebp-8], ebx
		inc esi
		jmp loop_function

	count_c:
		mov ecx,[ebp-12]
		inc ecx
		mov [ebp-12], ecx
		inc esi
		jmp loop_function
	letter ENDP
	start:
		sub esp, 12 ; creation 3 emplacement memoire pour a,b et c
		push offset mot
		call letter

		push ecx
		push ebx
		push eax
		push offset result
		call crt_printf
		add esp,16

		popad
		push 0
		call ExitProcess
	end start
