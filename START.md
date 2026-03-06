# Démarrer le Portfolio

## 1. Backend Django

```bash
cd portfolio-backend
# Activer l'environnement virtuel (depuis la racine ANGULAR) :
..\portfolio-venv\Scripts\activate   # Windows PowerShell
python manage.py runserver
```

- **API** : http://127.0.0.1:8000/api/
- **Documentation Swagger** : http://127.0.0.1:8000/api/schema/swagger-ui/
- **Admin** : http://127.0.0.1:8000/admin/

### Première fois : créer un superutilisateur

```bash
python manage.py createsuperuser
```

Puis allez sur http://127.0.0.1:8000/admin/ pour gérer vos données et **uploader vos images**.

## 2. Frontend Angular

```bash
cd portfolio-angular
npm start
```

- **Site** : http://localhost:4200

## 3. Ajouter des images

1. Démarrez le backend
2. Allez sur http://127.0.0.1:8000/admin/
3. Connectez-vous avec votre superuser
4. Dans **Portfolio > Projects**, modifiez chaque projet et uploadez une image
5. Dans **Portfolio > Profiles**, uploadez votre photo de profil

Les images sont stockées dans `portfolio-backend/media/` et servies via l'API.
