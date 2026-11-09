## FRONT
- client-side validation : error message if some input are missing (try to imagine what is the best in UI & accessibility terms) + required + patterns
- should I make a list of missing/incorrect fields ? or should a paragraph under inputs ? or a modal with incorrect fields ? how vocal assistants will deal with it ? 

Validation front :
Faire un nettoyage des alertes : plus propre, compatible assistant vocaux, messages d'alertes qui s'affichent près des champs concernés. 

## BACK
- HTTPonly token :
Mettre à jour les appels API côté front pour ajouter les credentials, retirer le document.cookie token=, retirer le authorization bearer. > MAJ à faire aussi côté Postman. 

Voir pour révoquer le token à la deconnexion.

Voir pour le refresh des token. 


- ratelimiter 