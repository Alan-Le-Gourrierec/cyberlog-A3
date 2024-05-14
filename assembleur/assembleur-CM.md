ADD
SUB
DIV
MUL
INC +1
DEC -1

AND, OR, XOR, NOT, CMP
LSL, LSR, ASR (décélage)

Registre généraux AX, BX, 
Registre d'index SI et DI
registre de pile : BP, SP
pointeur d'instructions: IP
registre de segment : CS, SS

taille info : 1 octet 
somme avec add

langage machine c sympa mais écrire en assembleur c plus fun et un peu moins pire

MASM

```risk5
ADD AX, BX

MOV eax, 32

EQU 80
EQU 25

```


on ne peux bouger que des registres

```
.386
.model flat, stdcall
option casemap:none

include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
includelib \masm32\lib\kernel32.lib

.data
    number1 DWORD 10
    number2 DWORD 20
    result DWORD ?

.code
main:
    ; Charge les valeurs des nombres dans les registres
    mov eax, number1
    add eax, number2
    mov result, eax
    
    ; Affiche le résultat
    invoke StdOut, ADDR result
    invoke ExitProcess, 0

end main
```

l'opérateur PTR permet de ne lire que la taille précisé en le précédent des opérateur suivant :
```
.data
    ; Déclaration d'une variable de type BYTE (1 octet)
    myByte BYTE 10

    ; Déclaration d'une variable de type WORD (2 octets)
    myWord WORD 1000

    ; Déclaration d'une variable de type DWORD (4 octets)
    myDword DWORD 123456

    ; Déclaration d'une variable de type QWORD (8 octets)
    myQword QWORD 1234567890123456

    ; Déclaration d'une variable de type REAL4 (nombre en virgule flottante sur 4 octets)
    myReal4 REAL4 3.14

    ; Déclaration d'une variable de type REAL8 (nombre en virgule flottante sur 8 octets)
    myReal8 REAL8 3.14159265358979323846

    ; Déclaration d'une chaîne de caractères (terminée par un zéro)
    myString BYTE "Hello, world!", 0

    ; Déclaration d'une chaîne de caractères avec longueur spécifiée
    myString2 BYTE "Hello", 0

    ; Déclaration d'un tableau de 10 éléments de type DWORD initialisé à 0
    myArray DWORD 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

```

décalage SHL et SHR (utile pour les multiplication par 2 ou les division par 2)

le prof fait des trucs chelou et dit qu'il fait du spurutisme


fonction JMP

permet d'aller à un emplacement mémoire.

On peu avoir de jmp de jmp, c'est marrant. Il y à la notion de stack aussi même si c évident
c pour l'ordre des action en gros. Faut la mémoriser et on met le truc au top de la S 

RET dépile l'address.

mov <a>, <b>
staock a dans le registre b
(mov eax, ebx)


add -> 626
mov -> 1256

add <a>, <b>
addition de a et b et on stock dans a
invoke existe pour un call de fct 

```asm
invok ExitProcess ,eax

même que 
push eax
call ExitProcess
```