# Guide de déploiement - Portfolio Océane Konan

Ce guide t’explique étape par étape comment déployer ton portfolio (backend Django + frontend Angular) en production.

> **📋 Version simplifiée :** Tu préfères une checklist à cocher ? Ouvre **DEPLOIEMENT_CHECKLIST.md**

---

## Vue d’ensemble

| Partie   | Technologie    | Plateforme | URL finale                    |
|----------|----------------|------------|-------------------------------|
| Backend  | Django REST    | Render.com | https://xxx.onrender.com      |
| Frontend | Angular        | Vercel     | https://xxx.vercel.app        |

**Ordre recommandé :** 1) Mettre le code sur GitHub → 2) Déployer le backend → 3) Déployer le frontend.

---

# Partie 1 : Préparer GitHub

## 1.1 Initialiser Git (si ce n’est pas déjà fait)

Dans le dossier `ANGULAR` (contenant `portfolio-backend` et `portfolio-angular`) :

```powershell
cd C:\Users\Oceane\Desktop\ANGULAR
git init
```

## 1.2 Créer un fichier `.gitignore` à la racine

Crée `C:\Users\Oceane\Desktop\ANGULAR\.gitignore` avec :

```
portfolio-backend/.env
portfolio-backend/__pycache__/
portfolio-backend/*.pyc
portfolio-backend/db.sqlite3
portfolio-backend/media/
portfolio-backend/staticfiles/
portfolio-backend/emails/
portfolio-angular/node_modules/
portfolio-angular/dist/
*.log
.venv/
venv/
```

## 1.3 Créer un dépôt sur GitHub

1. Va sur [github.com](https://github.com) et connecte-toi.
2. Clique sur **New repository**.
3. Nom : `ANGULAR_PORTFOLIO` (ou autre).
4. **Public**.
5. Ne coche pas "Add a README" (le projet existe déjà).
6. Clique sur **Create repository**.

## 1.4 Pousser le code

```powershell
cd C:\Users\Oceane\Desktop\ANGULAR
git add .
git commit -m "Initial commit - portfolio complet"
git branch -M main
git remote add origin https://github.com/Mocey2/ANGULAR_PORTFOLIO.git
git push -u origin main
```

---

# Partie 2 : Déployer le backend (Django) sur Render

## 2.1 Compte Render

1. Va sur [render.com](https://render.com) et crée un compte (possible avec GitHub).

## 2.2 Base de données PostgreSQL

1. Dans le **Dashboard Render**, clique sur **New +** → **PostgreSQL**.
2. Nom : `portfolio-db`.
3. Plan : **Free**.
4. Region : choisir la plus proche (ex. Frankfurt).
5. Clique sur **Create Database**.
6. Une fois créée, note l’**Internal Database URL** (tu en auras besoin).

## 2.3 Service web Django

1. Clique sur **New +** → **Web Service**.
2. Connecte ton dépôt GitHub (autorise Render si demandé).
3. Choisis le repo `ANGULAR_PORTFOLIO`.

### Configuration du service

| Champ             | Valeur                                                                 |
|-------------------|------------------------------------------------------------------------|
| **Name**          | `portfolio-backend`                                                    |
| **Region**        | Même que la base de données                                           |
| **Root Directory**| `portfolio-backend`                                                    |
| **Runtime**       | Python 3                                                              |
| **Build Command** | `./build.sh`                                                          |
| **Start Command** | `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`               |

### Variables d’environnement (Environment)

Clique sur **Environment** et ajoute :

| Key             | Value                                  |
|-----------------|----------------------------------------|
| `DATABASE_URL`  | Colle l’**Internal Database URL** de la base |
| `SECRET_KEY`    | Clique sur **Generate** pour générer   |
| `DEBUG`         | `False`                                |
| `FRONTEND_URL`  | `https://ton-frontend.vercel.app` (ajuste après déploiement du frontend) |
| `WEB_CONCURRENCY` | `2`                                 |

Pour l’email (optionnel) :

| Key                  | Value                      |
|----------------------|----------------------------|
| `EMAIL_BACKEND`      | `django.core.mail.backends.filebased.EmailBackend` |
| `CONTACT_RECIPIENT_EMAIL` | `gracemahouk@gmail.com` |

4. Plan : **Free**.
5. Clique sur **Create Web Service**.

## 2.4 Attendre le déploiement

Le premier déploiement peut prendre 5–10 minutes. Surveille les logs.

## 2.5 Créer un superutilisateur (admin Django)

Quand le service est déployé :

1. Ouvre ton service sur Render.
2. Va dans **Shell** (onglet).
3. Lance :

```bash
python manage.py createsuperuser
```

Entre un nom d’utilisateur, un email et un mot de passe.

## 2.6 Charger les données initiales

Si tu as un script de données (`load_initial_data.py`) :

```bash
python manage.py load_initial_data
```

Sinon, passe à l’étape suivante et crée les données via l’admin :  
https://TON-BACKEND.onrender.com/admin/

## 2.7 Médias (images)

Le stockage Render est temporaire : les fichiers uploadés peuvent disparaître au redéploiement.  
Pour l’instant, les images ajoutées via l’admin fonctionneront, mais seront perdues à chaque nouveau déploiement. Pour une solution durable, il faudrait plus tard un stockage type AWS S3 ou Cloudinary.

---

# Partie 3 : Déployer le frontend (Angular) sur Vercel

## 3.1 Mettre à jour l’URL de l’API

1. Ouvre `portfolio-angular/src/environments/environment.prod.ts`.
2. Remplace `TON-BACKEND-RENDER` par l’URL réelle de ton backend Render (sans `https://` ni `/api`).  
   Exemple : si ton backend est `https://portfolio-backend-abc123.onrender.com`, mets :

```ts
apiUrl: 'https://portfolio-backend-abc123.onrender.com/api',
```

3. Commit et push :

```powershell
git add .
git commit -m "Config API prod"
git push
```

## 3.2 Compte Vercel

1. Va sur [vercel.com](https://vercel.com) et connecte-toi avec GitHub.

## 3.3 Importer le projet

1. Clique sur **Add New** → **Project**.
2. Importe le dépôt `ANGULAR_PORTFOLIO`.

### Configuration

| Champ                 | Valeur                      |
|-----------------------|-----------------------------|
| **Framework Preset**  | Other                       |
| **Root Directory**    | `portfolio-angular`         |
| **Build Command**     | `npm run build`             |
| **Output Directory**  | `dist/portfolio/browser`    |
| **Install Command**   | `npm install`               |

3. Clique sur **Deploy**.

## 3.4 Récupérer l’URL du frontend

Quand le déploiement est terminé, tu obtiens une URL du type :  
`https://portfolio-oceane-xxx.vercel.app`

## 3.5 Mettre à jour le CORS côté backend

1. Sur Render, va dans ton service backend → **Environment**.
2. Modifie `FRONTEND_URL` et mets l’URL Vercel (ex. `https://portfolio-oceane-xxx.vercel.app`).
3. Sauvegarde (Render redéploiera si besoin).

---

# Partie 4 : Vérifier le déploiement

1. **Frontend :** Ouvre l’URL Vercel → le portfolio doit s’afficher.
2. **Backend :** Ouvre `https://TON-BACKEND.onrender.com/admin/` et connecte-toi.
3. **Contact :** Teste le formulaire de contact pour vérifier que l’envoi fonctionne.

---

# Résumé des URLs

- **Site :** https://ton-projet.vercel.app  
- **Admin :** https://ton-backend.onrender.com/admin/  
- **API :** https://ton-backend.onrender.com/api/

---

# Problèmes courants

## Le frontend affiche une page vide ou des erreurs

- Vérifie que `environment.prod.ts` pointe bien vers la bonne URL backend.
- Vérifie la console du navigateur (F12) pour les erreurs CORS ou 404.

## Erreur CORS

- Vérifie que `FRONTEND_URL` sur Render correspond exactement à l’URL Vercel (sans slash final).

## Les images ne s’affichent pas

- Sur Render, les médias sont temporaires. Recharge les images via l’admin après chaque redéploiement, ou prévois un stockage externe (S3, Cloudinary).

## Le backend est lent au premier chargement

- Le plan gratuit Render met le service en veille après ~15 min d’inactivité. Le premier chargement peut prendre environ 1 minute.

---

Bon déploiement.
