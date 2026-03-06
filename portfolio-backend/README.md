# Portfolio Backend - API Django REST

Backend Django REST Framework pour le portfolio dynamique d'Océane Konan.

## Installation

```bash
cd portfolio-backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

## Configuration

```bash
python manage.py migrate
python manage.py load_initial_data
python manage.py createsuperuser
```

## Lancer le serveur

```bash
python manage.py runserver
```

- **API** : http://127.0.0.1:8000/api/
- **Documentation Swagger** : http://127.0.0.1:8000/api/schema/swagger-ui/
- **Admin Django** : http://127.0.0.1:8000/admin/

## Endpoints API

| Méthode | URL | Description |
|---------|-----|-------------|
| GET | /api/profile/ | Profil |
| GET | /api/education/ | Formations |
| GET | /api/experience/ | Expériences |
| GET | /api/skills/ | Compétences |
| GET | /api/interests/ | Centres d'intérêt |
| GET | /api/projects/ | Projets (?type=academique ou personnel) |
| GET | /api/facts/ | Chiffres clés |
| POST | /api/contact/ | Envoyer un message (name, email, subject, message) |

## Images

Les images sont stockées dans `media/` :
- `media/profile/` : photo de profil
- `media/projects/` : images des projets

Uploadez vos images via l'admin Django (http://127.0.0.1:8000/admin/).
