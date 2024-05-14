calcule valeur future du cash flow :
$FV_0=PV(1+i)^n$
r```txt
```
avec FV = valeu future
n = periode d'investissement
i = interet
```

ceci permet de déterminer la valeur du retour sur investissement d'un placement. 

PV (valeur présent):
$PV = \frac{FV_n}{(1 + i)^n}$ 

calcule taux d'intérêt:
$i= (\frac{FV_n}{PV})^{\frac{1}{n}}-1$

amortissement des dettes(appelé annuité)
Les annuités sont constantes, 


| année | capital emprinté | intérets | principale | annuité |
| ---- | ---- | ---- | ---- | ---- |
| 1 | 20000 | 2200 | 3211.41 | 5411.41 |
| 2 | 16788.59 | 1846.74 | 3564.66 | 5411.41 |
| 3 | 13223.93 | 1454.63 | 3956.77 | 5411.41 |
| 4 | 9267.16 | 1019.38 | 4392.02 | 5411.41 |
| 5 | 4875.14 | 536.26 | 4875.14 | 5411.41 |
$capitalEmprinte = capitaleEmprinte_{-1}- principal$ 
$intrest = capitalEmprunte*i$
$annuite= \frac{(K* i)}{(1-(1+i)^{-n})}$   
$principale = annuite - interet$

investissement = actif imobilisé

![[Pasted image 20240129100050.png]]

EBIT = Revenus - COGS - Amortissements 

![[Pasted image 20240129101746.png]]

Correction 

| what | 0 | 1->6 | 7 |
| ---- | ---- | ---- | ---- |
| Revenus |  | 155000 | 15500 |
| - COGS |  | 100000 | 100000 |
| - depresiation |  | 8000 | 8000 |
| EBIT |  | 47000 | 47000 |
| - taxes (34%) |  | 15980 | 15980 |
| profits after taxes |  | 31020 | 31020 |
| + depresiation |  | 8000 | 8000 |
| - capital expends | 62000 |  |  |
| - NWCN |  |  |  |
| + Salvage Value  |  |  | 6000 |
| fcf | -62000 | 39020 | 45020 |
$depressiation =\frac{I - 6000}{n}$
avec I = 62000 (coût des machines + installation)
et n = 7 (noombre d'années)

$NPV = -62000 + \sum_{p = 1}^{6} 39020\times(1+0.15)^{-p} + 45020\times(1+0.15)^{-7}$  
ce qui est : revenu de la première année + la somme des revenu sur les 6 année (avec déprésiation) + les revenu de la dernière année

---
 ![[Pasted image 20240129105228.png]]

<b>Pour tous, r = 10%</b>

 #### Machine A 
 
|  | FCF |
| ---- | ---- |
| 0 | -100000 |
| 1 | 40000 |
| 2 | 40000 |
| 3 | 40000 |
| 4 | 40000 |
NPV = 26794 (ou $NPV = -100000 + \sum_{p = 1}^{4} 40000 \times (1 + r)^{-p}$)
$a = PV\times \frac{i}{1 - 1(1+i)^{-N}}$ = 8452.92

#### Machine B
|  | FCF |
| ---- | ---- |
| 0 | -65000 |
| 1 | 35000 |
| 2 | 35000 |
| 3 | 35000 |
NPV = 22039 (ou $NPV = -65000 + \sum_{p = 1}^{3} 35000 \times (1 + r)^{-p}$) 
a = 8862.54

---
$I = \sum^{PB} CP_p \times(1+a)^{-p}$ 

Ceci permet de déterminer en combien de temps le projet va être rentabilisé, pour se faire, nous allons regarder quand notre Investisement (I) sera remboursé avec $CF_p$ le retour sur investissement. 

I = 2324000
$CF_p = 600000$ 
a = 11%
![[Pasted image 20240129113453.png]]

| Projet |  | Cash Flows |  |  |
| ---- | ---- | ---- | ---- | ---- |
|  | t = 0 | t = 1 | t = 2 | t = 3 |
| A | -2000 | 500 | 500 | 5000 |
| B | -2000 | 500 | 1800 | 0 |
| C | -2000 | 1800 | 0 | 0 |
![[Pasted image 20240129115101.png]]

IRR => NPV = 0