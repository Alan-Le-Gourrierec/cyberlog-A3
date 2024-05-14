use permet de faire des description textuel basé sur la définition de classe plus les contraintes sur le diagramme. 
état du systhème; état du système à un instant t

use possède deux interface :
- graphique
- ligne de commandes 

La structure du fichier :

#### enumération

```use
enum<enumerationname>{n1,...,nn}
```

#### les classes 

```use
[abstract] class <classname>
[attributes {atributename:type}]
[operation{<operationdeladeclaration>[=<oclexpresion>]}]
[ constraints { <invariantdefinition> } ]
end

```

<U>exemple :</U>
![[Pasted image 20231124164015.png]]

#### associations, compositions et agrégations

```use
Associations, compositions et aggregations
8
( association | composition | aggregation ) <associationname> between
<classname> [ <multiplicity> ] [ role <rolename> ] [ ordered ]
<classname> [ <multiplicity> ] [ role <rolename> ] [ ordered ]
{ <classname> [ <multiplicity> ] [ role <rolename> ] [ ordered ] }
end
```

![[Pasted image 20231124164807.png]]

#### association 
```use
[abstract ] associationclass <classname> between
<classname> [ <multiplicity> ] [ role <rolename> ] [ ordered ]
<classname> [ <multiplicity> ] [ role <rolename> ] [ ordered ]
<classname> [ <multiplicity> ] [ role <rolename> ] [ ordered ]
[ attributes { <attributename> : <type> } ]
[ operations { <operationdeclaration> [ = <oclexpression> ]
{ <preconditiondefinition> | <postconditiondefinition> } } ]
[ constraints { <invariantdefinition> } ]
end
```

#### contrainte

```use
Constraints
Context Classename
Inv constraintname : OCLexpression
…….
Context Classename::operation(parametres) : retType
Pre constraintname : OCLexpression
Post constraintname : OCLexpression
......
```

![[Pasted image 20231124165335.png]]

result => valeur retourné par la méthode (en gros c'est un ptn de return)

