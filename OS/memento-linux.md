Durant le TP de system d'exploitation, j'était l'utilisateur linux. Je vais donc présenter les divers commandes que j'ai utilisé : (les exemples, captures d'écrans viennent de mon système d'ou un affichage légèrement différent du à zsh)
## <font color = magenta> Commandes de base </font>

### Commande pour lister les dossier dans le répertoire ou nous nous trouvons ?
```bash
ls 
```

Une "variante" existe pour ce dernier afin d'afficher les dossier cacher et les permissions pour chaque utilisateurs qui est :
```bash
ls -la
```

![[Pasted image 20231203180853.png]]

Nous pouvons également utiliser cette même commande suivie d'un nom de repertoire pour afficher ce qu'il s'y trouve (et ceci marche aussi avec le -la)
```bash
ls nom_du_repertoire
```

![[Pasted image 20231203181239.png]]

---
### Se déplacer de répertoire en répertoire
Pour changer de repertoire, nous utilisons la commande suivante :
```bash
cd nom_du_repertoire
```

Il y à aussi trois répertoire "spéciaux" pour lesquelles nous pouvons y retourner en une commande : 
- notre homme (fichier ou nous nous trouvons au lancement du terminal)
```bash
cd ~
```
ou 
```bash
cd
```
- la root (racine, la base ou se trouvent tout les fichiers)
```bash
cd /
```
- se déplacer au répertoire précédent :
```bash
cd ..   #nous pouvons ajouter des /.. pour revenir plusieur répertoire avant
```

---
### Suppression fichier ou répertoire
Pour supprimer un fichier nous utilisons la commande :
```bash
rm nom_du_fichier
```

Pour un répertoire nous pouvons utiliser si il est vide :
```bash
rmdir nom_du_repertoire
```

Sinon nous pouvons utiliser :
```bash
rm -r nom_du_repertoire
```

---
### Droit super utilisateur 
Parfois, nous n'avons pas les droits pour exécuter une action, comme mettre à jour le système ou modifier des fichiers root. Pour se faire, nous utilisons la commande suivante :
```bash
sudo
```
qui nous donne les permission administrateurs sur toutes nos commandes comme pour mettre à jour notre système :

```bash
sudo apt update     #met à jour les répots de debian de le but de mettre à jour
sudo apt upgrade    #met à jour le systhème
```

Cette commande n'est pas relative à tout les OS linux. Elle n'est relative que à ceux utilisant apt. Par exemple Archlinux (le meilleur OS) utilise pacman et pour mettre à jour le système nous utilisons :
```bash
sudo pacman -Suy
```

Ou pour ceux l'ayant [installé](https://www.linuxadictos.com/fr/yay-como-instalar-este-asistente-de-aur-en-distros-basadas-en-arch-linux.html) nous pouvons utiliser la commande suivante :
```bash
yay -Suy
```

(Il y a d'autre gestionnaires de packet mais je n'ai fait que prendre un autre exemple) 

---
### Modification des droits pour un fichier

En parlant de droits super utilisateurs, nous pouvons aussi une commande pour changer les divers droits (exécution, read, write) avec la commande suivante :
```bash
chmod code_des_droits nom_du_fichier
```

Pour obtenir les code à entrer, je vous recommande de regarder sur ce [site](https://chmod-calculator.com/). Si nous voulons faire au plus simple, nous pouvons mettre le code 777 afin de donner toutes les permission à tout les utilisateur (<b>ce qui peu créer de problèmes de sécurité !!</b>). 

---
### afficher le contenu d'un fichier

Pour afficher le contenu d'un fichier, nous utilisons la commande suivante :
```bash
cat nom_du_fichier
```

Nous obtenons ceci :
![[Pasted image 20231203190523.png]]

---
### Vim
Comme autre commande majeur que j'ai utilisé, il y à vim, plus précisément neovim. Ceci est un éditeur de texte qui s'installe avec la commande suivante:
```bash
sudo apt install vim neovim
```

Pour l'utiliser suite à l'installation, il nous suffit de faire :
```bash
nvim nom_du_fichier
```
Si ce dernier n'existe pas, alors il le créeras, donc nous ne somme pas obliger d'utiliser la commande :
```bash
touch nom_du_fichier
```
Pour en créer un.

Pour son utilisation, je vous envoie vers une documentation de [vim](https://linux-note.com/vim-raccourcis-clavier/) mais les commandes les plus utilisé (en mode normale en fessant ctrl + c) sont :

commande |  effet 
---|---
yy | copier la ligne
dd | couper la ligne
i | basculer en mode insertion
p | coller
u | annuler la dernière action (comme un ctrl + z)
ctrl + r | refaire la dernière action annulé (comme un crl + y)
:w | sauvegarder le fichier
:q | quitter le fichier

---
### Copier et déplacer un fichier (ou répertoire)

Pour copier un fichier (ou un répertoire), nous utilisons la commande suivante :
```bash
cp nom_du_fichier nom_de_la_copie
```

Nous pouvons aussi le copier dans un autre répertoire :
```bash
cp nom_du_fichier path/du/fichier/puis_son_nom
```

pour déplacer un fichier (ou répertoire) nous utilisons la commande suivante :
```bash
mv nom_du_fichier edroit/ou/va/se/trouver/le/fichier
```

Nous pouvons aussi renommer les fichier grâce à cette commande avec :
```bash
mv nom_du_fichier nouveau_nom
```
---
### Documentation de la commande

Pour obtenir la documentation d'une commande, nous pouvons :
- demander à chatgpt qui feras les recherche à notre place et nous diras quoi faire exactement (ce qui est ~~toujours~~ rarement utilisé par les étudiants )
- chercher sur internet 
- utiliser une commande 

Cette comamnde est la commande suivante :
```bash
man la_commande
```

---
### Réseau et IP

Pour afficher notre ip, notre adresse mac et l'interface correspondant à cette dernière, nous utilisons la commande :
```bash
ip a
```
![[Capture d’écran du 2023-12-03 19-19-29.png]]

---
### Exécution fichier en C

Pour se faire, dans un premier temps, nous allons installer gcc avec la commande suivante :
```bash
sudo apt install gcc
```

Une fois ceci fait et un fichier en C crée et fonctionnel comme :
```c
#include <stdio.h>

int main()
{
	printf("Hello World !!");
	return 0;
}
```
(un programme d'une grande complexité)

Ce programme est nommé **helloworld.c** et pour le compiler, nous allons utiliser la commande suivante :
```bash
gcc -o helloworld.o helloworld.c
```

et allons obtenir un exécutable qui est **helloworld.o**. Pour l’exécuter, nous utiliserons la commande suivante :
```bash
./helloworld.o
```


