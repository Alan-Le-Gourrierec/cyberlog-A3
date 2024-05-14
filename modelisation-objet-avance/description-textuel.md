### Consulter les produits 
- **nom du cas** : Consulter les produits
- **Objectif** : Permettre à un utilisateur de consulter la liste des produits sur le site.
- **Acteurs** : fournisseur, internaute, client, administrateur
- **Date** : 08/04/24
- **Responsable** : Alan Le Gourrierec
- **Version** : 1.1
- **Pré-condition** : Le site est fonctionnel et les produits sont présents sur ce dernier
- **Scénario nominal** :
	1. L'utilisateur arrive sur la page d’accueil
	2. l'utilisateur recherche un produit dans la barre de recherche multicritère ou sur l'écran d’accueil 
	4. l'utilisateur sélectionne un produit sur le site
	5. le système affiche les informations relatives à ce produit : nom, marque, description, image représentant le produit, le prix et sa disponibilité
- **Enchaînements alternatifs** :
	- la recherche sur le site ne renvoie aucun résultat. Le système envoie donc un message spécifiant que la recherche n'a pas abouti
	- le produit n'est plus disponible. Ses stock sont donc à 0 
- **Post-Condition** : l'utilisateur peut continuer à faire des recherches sur le site

### Ajouter un produit au panier
- **nom du cas** : ajouter un produit au panier
- **Objectif** : Permet à l'utilisateur d'ajouter un produit à son panier
- **Acteurs** : client
- **Date** : 08/04/24
- **Responsable** : Alan Le Gourrierec
- **Version** : 1.0
- **Pré-condition** : Le site est fonctionnel et le client s'est authentifié sur le site. Les produits sont aussi disponibles sur le site.
- **Scénario nominal** : 
	1. le client est sur la page d'un produit 
	2. le client sélectionne la quantité souhaitée du produit
	3. le système ajoute la quantité du produit en question au panier de l'utilisateur
- **Enchaînement alternatifs** :
	- le client ajoute une quantité supérieure à celle en stock : nous prévenons l'utilisateur et nous mettons la quantité maximale disponible à la place de la quantité entrée.
	- le client annule l'ajout
- **Post-condition** : le produit est ajouté au panier de l'utilisateur

### Passer une commande en ligne
- **nom du cas** : passer une commande en ligne
- **Objectif** : permettre à l'utilisateur de finaliser sa commande 
- **Acteurs** : client
- **Date** : 08/04/24
- **Responsable** : Alan Le Gourrierec
- **Version** : 1.0
- **Pré-condition** :le système est fonctionnel, le client s'est authentifié, les produits sont disponible et la carte bancaire de l'utilisateur est valide
- **Scénario nominal** : 
	1. le client clique sur son panier
	2. le client valide le contenu de son panier
	3. le système demande au client de renseigner les informations de livraison de l'utilisateur et ses informations de paiement 
	4. le client saisit les information demandées par le système
	5. le système valide la commande et l'informe par un message que la procédure est validée
- **Enchaînement alternatifs** :
	- les informations entrées par le client sont invalides : le système informe l'utilisateur quels champs sont erronés et demande à l'utilisateur de palier ces erreurs
	- le client n'a pas le montant suffisant pour valider la commande : le système informe le client et le fait retourner sur la page ou ce dernier doit entrer ses informations bancaires
	- le client abandonne la commande : le système renvoie l'utilisateur sur l'écran d’accueil et informe par le message "commande annulée"
- **Post-condition** :  la commande est finalisée, elle est donc enregistrée

### Gérer les réclamations
- **nom du cas** : Gérer les réclamations
- **Objectif** : permettre à l'utilisateur (client) de contacter un administrateur
- **Acteurs** : client (principal), administrateur (secondaire)
- **Date** : 08/04/24
- **Responsable** : Alan Le Gourrierec
- **Version** : 1.0
- **Pré-condition** : le client s'est authentifié et a passé au moins une commande
- **Scénario nominal** : 
	1. le client lève un ticket concernant un/des produit(s) avec les informations relatives (brève description) de la raison du renvoi
	2. le client choisit si il préfère un remboursement ou un échange
	3. le système envoie une requête aux administrateurs pour la traiter
	4. l'administrateur consulte le ticket et contacte le client. Il peut aussi passer à un remboursement. 
- **Enchaînement alternatifs** :
	- Pas de réclamation en cours : le système informe l'utilisateur qu'il n'a aucune réclamation en cours
- **Post-condition** : les réclamations sont enregistrées dans le système et un administrateur traite la demande

### Ajouter un produit à la plateforme
- **nom du cas** : Ajouter un produit à la plateforme
- **Objectif** : permettre à l'utilisateur d'ajouter un produit 
- **Acteurs** : fournisseur
- **Date** : 08/04/24
- **Responsable** : Alan Le Gourrierec
- **Version** : 1.0
- **Pré-condition** : le fournisseur est certifié et s'est authentifié sur la plateforme
- **Scénario nominal** : 
	1. le fournisseur accède à l'écran d'ajout de produit 
	2. le fournisseur clique sur "ajouter un produit "
	3. le système affiche un formulaire à remplir pour ajouter, une description, un prix, une image, un nom, une marque et une quantité
	4. le fournisseur valide le formulaire
	5. le système enregistre la demande dans une base de donnée
- **Enchaînement alternatif** : 
	- Le fournisseur ne remplit pas bien les champs : un message affichant une erreur apparaît et le système informe en changeant la couleur en rouge que le champ n'est pas correctement remplit
	- le produit a déjà été ajouté dans le système : le système informe que ce produit existe déjà et demande au fournisseur de vérifier les informations
- **Post-condition** : Le produit a été ajouté au site et est visible par tous les utilisateurs