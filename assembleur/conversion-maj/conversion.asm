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

section .data
    str db "hello world", 0  ; Chaîne de caractères en minuscules
    len equ $ - str           ; Calcul de la longueur de la chaîne
    
section .text
    global _start

_start:
    ; Appel de la routine pour mettre la chaîne en majuscules
    mov esi, str       ; Pointeur de source (chaîne d'entrée)
    call to_uppercase  ; Appel de la routine de conversion en majuscules
    
    ; Affichage de la chaîne convertie
    mov eax, 4         ; Appel système pour l'affichage (write)
    mov ebx, 1         ; Descripteur de fichier (stdout)
    mov ecx, str       ; Adresse de la chaîne convertie
    mov edx, len       ; Longueur de la chaîne
    int 0x80           ; Appel du noyau Linux
    
    ; Terminaison du programme
    mov eax, 1         ; Appel système pour la sortie (exit)
    xor ebx, ebx       ; Code de retour (0 pour indiquer le succès)
    int 0x80           ; Appel du noyau Linux

    mov eax, 0
    invoke	ExitProcess,eax

to_uppercase:
    push ebp
    mov ebp, esp
    push ebx
    push ecx
    
    ; Parcourir la chaîne caractère par caractère
    mov ecx, len
    mov ebx, esi       ; Sauvegarde du pointeur de départ
    
convert_loop:
    mov al, [esi]      ; Charger le caractère dans AL
    cmp al, 0          ; Vérifier si c'est la fin de la chaîne
    je end_conversion  ; Si c'est la fin, terminer
    
    cmp al, 'a'        ; Comparer avec 'a'
    jb skip_conversion ; Si le caractère est plus petit que 'a', passer à la prochaine itération
    
    cmp al, 'z'        ; Comparer avec 'z'
    ja skip_conversion ; Si le caractère est plus grand que 'z', passer à la prochaine itération
    
    sub al, 32         ; Convertir en majuscule (32 est la différence entre 'a' et 'A')
    mov [esi], al      ; Mettre à jour le caractère dans la chaîne
    
skip_conversion:
    inc esi            ; Passer au caractère suivant
    loop convert_loop  ; Répéter jusqu'à la fin de la chaîne
    
end_conversion:
    pop ecx
    pop ebx
    pop ebp
    ret
