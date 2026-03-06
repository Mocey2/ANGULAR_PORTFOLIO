# Démarrer le Portfolio

> **Important :** Les deux serveurs doivent tourner **en même temps** pour que le portfolio affiche toutes les données.

---

## Option 1 : Lancer les deux (2 terminaux)

### Terminal 1 — Backend (obligatoire)

```powershell
cd C:\Users\Oceane\Desktop\ANGULAR
& portfolio-venv\Scripts\Activate.ps1
cd portfolio-backend
python manage.py runserver
```

Laisse ce terminal ouvert. Le backend tourne sur **http://127.0.0.1:8000**

### Terminal 2 — Frontend

```powershell
cd C:\Users\Oceane\Desktop\ANGULAR
cd portfolio-angular
npm start
```

Le site s’ouvre sur **http://localhost:4200**

---

## Première fois uniquement

### 1. Installer les dépendances du backend

```powershell
cd C:\Users\Oceane\Desktop\ANGULAR
& portfolio-venv\Scripts\Activate.ps1
cd portfolio-backend
pip install -r requirements.txt
```

### 2. Charger les données initiales (profil, projets, compétences, etc.)

```powershell
cd C:\Users\Oceane\Desktop\ANGULAR
& portfolio-venv\Scripts\Activate.ps1
cd portfolio-backend
python manage.py migrate
python manage.py load_initial_data
```

### 3. Créer un compte admin (pour uploader les images)

```powershell
python manage.py createsuperuser
```

Entre un nom d’utilisateur, un email et un mot de passe.

### 4. Ajouter les images

1. Lance le backend (Terminal 1)
2. Va sur **http://127.0.0.1:8000/admin/**
3. Connecte-toi avec le superutilisateur
4. **Portfolio > Profiles** → modifie le profil et uploade ta photo
5. **Portfolio > Projects** → pour chaque projet, uploade une image

---

## Liens utiles

| Page        | URL                                |
|-------------|------------------------------------|
| **Site**    | http://localhost:4200              |
| **API**     | http://127.0.0.1:8000/api/         |
| **Admin**   | http://127.0.0.1:8000/admin/       |
| **Swagger** | http://127.0.0.1:8000/api/schema/swagger-ui/ |
