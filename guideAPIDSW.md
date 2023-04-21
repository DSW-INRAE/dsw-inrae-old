# P'tit guide API DSW
Ce document n'a pas pour objectif de remplacer l'API DSW, il sert juste à synthétiser et expliquer les requêtes qui nous sont utiles pour la réalisation de notre client DSW.
## Token
- **POST** ``/tokens`` : permet d'obtenir le token d'identification de l'utilisateur. 

Le body doit être  : 
```json
{
  "code": null,
  "email": "mail@mail.com",
  "password": "mdp"
}
```
Le retour sera : 
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZXJzaW9uIjoiMyIsInRva2VuVXVpZCI6ImIzM2FlYWIwLTNmYzUtNGMxMC05NDIyLTFmNWU3YjE0ODBjYyIsInVzZXJVdWlkIjoiZWM2ZjhlOTAtMmE5MS00OWVjLWFhM2YtOWVhYjIyNjdmYzY2IiwiZXhwIjoyNTMwMjcyMTE2fQ.JWcI1aouNXXRdRcFmIvHzy0QXChWcgbD1_bfJSlAFgw",
  "type": "UserToken"
}
```
Ne nécessite aucun droits.

## User
- **GET** ``/users`` : accède à l'ensemble des utilisateurs
Nécessite la permission **UM_PERM**
## Packages
Correspond aux KM
## Questionnaires
Correspond aux projets/PGD
## Permissions (spéculatif)
- **UM_PERM** : *user management permissions*, permet l'administration (visualisation, modification, suppression) des utilisateurs
