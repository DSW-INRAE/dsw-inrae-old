# P'tit guide API DSW
Ce document n'a pas pour objectif de remplacer l'API DSW, il sert juste à synthétiser et expliquer les requêtes qui nous sont utiles pour la réalisation de notre client DSW.
## Token
### **POST** ``/tokens``
*Permet d'obtenir le token d'identification de l'utilisateur.*
Le corps de la requête doit contenir un **UserTokenCreateDTO**.
Cela renverra un **UserTokenDTO**.
Ne nécessite aucun droits.

Dorénavant, pour l'ensemble des requêtes nécessitant des droits, il faudra inclure dans le champ *Authorization* de l'entête avec le token reçu à la place de ``{UserToken}`` : 
```json
"Bearer {UserToken}"
```
Dans notre cas, le champ *Authorization* sera donc : 
```json
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZXJzaW9uIjoiMyIsInRva2VuVXVpZCI6ImIzM2FlYWIwLTNmYzUtNGMxMC05NDIyLTFmNWU3YjE0ODBjYyIsInVzZXJVdWlkIjoiZWM2ZjhlOTAtMmE5MS00OWVjLWFhM2YtOWVhYjIyNjdmYzY2IiwiZXhwIjoyNTMwMjcyMTE2fQ.JWcI1aouNXXRdRcFmIvHzy0QXChWcgbD1_bfJSlAFgw"
```

## User
### **GET** ``/users`` : 
*Accède à l'ensemble des utilisateurs.*
Réponse : 
```json
{
    "_embedded": {
        "users": []
    },
    "page": {
        "number": 0,
        "size": 20,
        "totalElements": 5,
        "totalPages": 1
    }
}
```
Nécessite la permission **UM_PERM**.

### **GET** ``/users/current`` : 
*Accède à l'utilisateur courant*.
Renvoie un **UserDTO**.

### **POST** ``/users`` : 
*Créé un utilisateur à partir d'un **UserCreateDTO**.*
Ne nécessite aucun droit, l'utilisateur sera inactif par défaut et il aura le rôle *dataStewart*.

### **PUT** ``/users/current`` : 
*Modifie l'utilisateur courant à partir d'un **UserChangeDTO** dans le corps de la requête* 

### **PUT** ``/users/current/password`` : 
*Modifie le mot de passe de l'utilisateur courant à partir d'un **UserPasswordDTO***.

### **PUT** ``/users/{uUuid}`` : 
*Modifie l'utilisateur d'ID {uUuid} à partir d'un **UserChangeDTO** dans le corps de la requête* 
Nécessite la permission **UM_PERM**.

### **PUT** ``/users/{uUuid}/state``
*Change l'état d'activité de l'utilisateur d'ID {uUuid} à partir d'un **UserStateDTO***.

## Packages
Correspond aux KM
## Questionnaires
Correspond aux projets/PGD

## Permissions
- **UM_PERM** : *user management permissions*, permet l'administration (visualisation, modification, suppression) des utilisateurs
