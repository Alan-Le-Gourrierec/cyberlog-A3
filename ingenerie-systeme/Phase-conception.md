[[AFB-Analyse-Fonctionnelle-du-Besoin]]
## Phase 

Numéro | Phases | Description 
---|---|---
1 |Services en Maintenances | Le serveur est en maintenance, l'utilisateur ne peux donc pas se connecter 
2 | Services disponibles | Le service est dans son fonctionnement normale
2.1| Service Libre | Pendant cette sous phase le service marche de manière correct et les utilisateurs peuvent s'y connecté de façons normale   
2.2| Service Dégradé | Le service à un problème, l'utilisateur ne peux pas s'y connecté correctement, il y à donc une erreur
2.3 | Service Occupé | Le service est surchargé, il ne peux donc pas fonctionner à son plein potentiel

## Matrice des phases

/ | Service Libre | Service Occupé | Service Dégradé
---|---|---|---
2.1 Service Libre | / | Il n'y a pas suffisament de ressources allouables au nouvel utilisateur, le service marche donc au ralenti | Le service ne fonctionne plus, il passe donc en maintenance
2.2 Service Occupé | Le service n'est plus surchargé, il peut donc maintenant fonctionner à son plein potentiel (INFINITE POWER) | / | Le service ne fonctione plus, il passe donc en maintenance
2.3 Service Dégradé | Plus de pannes, plus de problèmes | NA | / 

---
### Scénario 1 : consultation des notes, cas optimal 20h15
  
La plateforme de note reçoit une requête de la part de Kevin Durand, élève de licence 1 en éco-gestion dans la moyenne et cherchant à se connecter pour consulter ses notes de mathématiques car le professeur a dit avoir corrigé les copies.

La plateforme lui renvoie alors la page d’accueil. Celle-ci comporte différentes matières, dont celle recherchée. La plateforme reçoit une requête vers la page maths. Il parvient donc à observer ses derniers résultats (2.5/20, il est en eco-gestion. Il se dit qu’il a une super note).

La plateforme reçoit une requête de déconnexion et déconnecte ce cancre.

La plateforme reçoit une requête de connexion de Maria Durand, mère de Kévin. Voulant regarder les notes de son fils. La plateforme est claire et elle trouve rapidement les notes de son fils. La plateforme reçoit une requête de déconnexion et déconnecte Maria.

### Scénario 2 : mise en maintenance 10/09/2017 à 10h37 

La plateforme de note reçoit une requête de la part de Kevin Durand afin de se connecter. 

Kevin Durand remarque que le site n’accepte pas les accents aigus et le moindre message écrit avec cet élément renvoie un “@#” à la place : “quand vous aurez mang@#, veuillez me rejoindre en S201”

La plateforme reçoit donc une demande de contact par Kévin cliquant sur le point d’interrogation pour transmettre sa demande vers un administrateur précisant ce problème.

La plateforme envoie donc un mail contenant ce qu’a entré Kévin.

La plateforme de note reçoit une requête d’un Bertrand Léveillé âgé de 44 ans qui essaie de se connecter pour constater le problème transmis par Kévin.

La plateforme de note reçoit une demande de Bertrand L@#veill@# enregistrant une note avec un descriptif contenant des actions.

La plateforme de note reçoit une requête d’un Bertrand L@#veill@# afin de rajouter sur l’ordre du jour de la prochaine réunion mensuelle ce problème.

La plateforme émet une notification à l'intention des autres administrateurs et du chef en question.

La plateforme reçoit une demande d’un administrateur afin de passer la plateforme en maintenance.

Par une procédure prédéfinie précédemment l’accès à l’identification est bloqué et un message est affiché : “Le service est en maintenance entre 14h et 22h30, veuillez réessayer ultérieurement”

La plateforme reçoit une demande de connexion de Kévin et affiche le message “Le service est en maintenance entre 14h et 22h30, veuillez réessayer ultérieurement”. Kévin rage, FORT.
  
La plateforme reçoit une requête de Michèle Kervzerski, une professeure de français, 40 ans et célibataire (célibatante comme elle se désigne  #attachiante), afin de déposer les notes de dissertation. Elle ne peut pas accéder à la plateforme moodle pour déposer les notes de ses copies devant être corrigées depuis plus de 4 mois

### scénario 3 : prof qui rentre sa note 28/04/2019 à 14h32

Il y a bien longtemps, dans une galaxie lointaine, très lointaine… En tant que plateforme de note, je reçois une requête de la part de ce cher professeur, le Compte Doucou (ça fait 2 semaines que ses élèves la harcèlent pour avoir les notes). Je lui renvoie donc la page d'accueil, qui comporte les matières qui lui sont associées. je reçois une requête pour la page OCaml (langage d’esti d’coliss de tabarnak de mardement incroyable) (PROPAGANDE DE MARGAUX RICHARD)

. Je reçois ensuite une requête pour ajouter les notes. le Compte Doucou, les ajoute 1 à 1 pour chaque élève.

- Maxime², 20²/20 .
- Margaux Richard, 21/20.
- Ewan, 8 (gro nul/20).
- Margaux ρ, N/A.
- Alan, langage DE MEEEEEEERDENIALISSIME ET QUAND MÊME TROP BIEN ON ADORE /20 !!!. (PROPAGANDE DE MARGAUX RICHARD)
- Baptiste, moins de pas mal/20.
- Hélène et les garçons. en cours d'acquisition/20
- Jean-Eude qui-es-tu/20
- Pierre, majoration/20
- Ayoub 4/20
- Joseph, tema la grosse dadidouille/20.
![](https://lh7-us.googleusercontent.com/u_FCxiLSl3v34BHUuKVGPzSpp3akYci3BGdDYxm8EsTzgTD-arULvi6KJiVZTG2KZQwXi8avpUKa6n-HXfOAzCnP5a51sQtcY2cbHLZKtRFU-E7VFBz8CdpUrJsRuwAhr4_qFHSUImbPIzUP8qE72Uo)
ROI DADIDOU quand il va te mettre la DADIDOUILLE

### Scénario 4 : un pirate essaye de modifier les notes de la plateforme 23/08/2021 à 17h02

xxX_DarkSasuke_Xxx en 4éme G  ayant eu 4/20 en espagnol souhaite pirater la plateforme afin de modifier sa note. Il se connecte avec son propre compte. Il utilise un logiciel téléchargé sur internet lui permettant de se faire passer en mode administrateur (et lui donnant 12 virus vu que c’était sur un site russe). Il finit donc par réussir à modifier sa note. Cependant le professeur d’espagnol reçoit un message de modification de note et se rend compte de la supercherie. La plateforme retrouve le compte associé à cette étrange modification et xxX_DarkSasuke_Xxx (pour garder son anonymat) se fait attraper et renvoyer pendant 3 jours.

### Scénario 5  12/11/2018 à 15h22

Aujourd’hui un événement grave s’est déroulé, Jean Eude, buvant sa bière durant ses heures de travail, sentit une odeur de brûlé. LES SERVEUR BRÛLAIENT !!! Un drame incommensurable, un désastre, non, une catastrophe digne des pires films catastrophes s’étant déroulé. 

Tous les étudiants tel xXX_darkSasuke2_Xxx, communément nommé Kevin Durant ont perdu leurs superbes notes. L’UBS a donc dû trouver une solution et cette dernière fut rapide, il faut trouver un nouvel hébergeur, mais pas OBS vu que ça brûle encore plus souvent que les nôtres. 

Ce désastre avait failli mettre en péril la stabilité de l’UBS, mais grâce à la grande intelligence de la DSI ce drame fut évité grâce à une sauvegarde sur un serveur externe. Vive la DSI, VIVE LA FRANCE !!!!

---
## Table des Intéracteurs

Références | Désignation | Déscription 
---|---|---
1 | Maintenance 
1.1 | Responsable DSI | décide les modifications à apporter à la plateforme et préside les réunions sur les éventuelles améliorations
1.2 | agent DSI | Applique les modifications précédemment définie
2 | Utilisateurs lecteur | possède les droits de consulter les notes qui lui sont associés
2.1 | Élève | Consultation uniquement des notes qui lui sont associés
2.2 | Parent d'élèves | Consultation uniquement des notes associées à son ou ses enfant(s)
3 | Utilisateurs écriture |
3.1 | Professeur | - possède les droits d’ajouter des notes / possède les droits de modifier les notes
3.2 | Administrateur de l'établissement | possède le droit de mettre F à une matière en cas d’absence récurrente
4 | Services exterieurs | 
4.1 | Pompier | 
4.2 | Policiers

