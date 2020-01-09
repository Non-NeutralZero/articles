# Comment documenter ?
Les mêmes principes et critères d’un bon code devraient s’appliquer à la documentation: 
- **Conventionnelle**
- **Simple**
- **Facile à comprendre**

En plus des critères d’un bon code, une bonne documentation devrait aussi être:
- **Explicative** (intention du code, règles métiers, clarification du code, mise en garde sur les conséquences d’une mauvaise utilisation, indications pour le testing)
- **Non-redondante**

```scala
/** 
  *Returns score
  */
int get_core(void){return score;}
```

- **Non-bruitée**
```scala
/**
 * Always returns true.
 */
 public boolean isTrue()
 { return false;}
 ```
 # Bonnes pratiques
 1. Introduire son code
 
 Décrire le contexte ou le background du code est une bonne pratique qui permettra aux lecteurs de se positionner par rapport aux conditions dans lesquelles le code a été généré et à ses objectifs.
 
 2. Connaître son public! 
 
 Avant de documenter, le développeur doit se poser la question: “qui sont/seront mes lecteurs?”. Une documentation visant un nettoyeur de données (focus ici sur les règles métiers par exemple) est différente d’une documentation visant un analyste de donnée (focus sur comment utiliser le code par exemple)
 
 3. Alerter sur les dépendances
 
 Lister et décrire les perspectives du code.
 
 4. “No comment out”
 
 i.e. Ne jamais retirer des lignes de documentation! 
 Si la documentation est bien faite et le code ne suit pas (à cause d’un refactor ou d’une modification), cela veut dire que le code ne fonctionne plus et qu’il devrait être supprimé ou lourdement remanié.
 
 5. Laisser des exemples
 
 Être gentil en laissant des exemples! Nice developers leave nice examples :) 
 
 6. KID - keep it documented! 
 
 Un refactor ou modification sans revue de documentation veut juste dire que le développeur n’a rien compris à ce document!
 
 

