## FRONT
- client-side validation : error message if some input are missing (try to imagine what is the best in UI & accessibility terms) + required + patterns
- should I make a list of missing/incorrect fields ? or should a paragraph under inputs ? or a modal with incorrect fields ? how vocal assistants will deal with it ? 

Required field policy :
- consider having some optional fields = pydantics needs to be modified.

Validation front :
Il faudrait ajouter une vérification pour qu'au moins un thème soit coché. 

## BACK
- HTTPonly token
- ratelimiter 