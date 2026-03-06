# ✅ Checklist de déploiement - Portfolio Océane

**Temps estimé :** 30 à 45 minutes

---

## Avant de commencer

- [ ] Compte GitHub (déjà fait ✓)
- [ ] Repo poussé : https://github.com/Mocey2/ANGULAR_PORTFOLIO ✓
- [ ] Créer un compte sur [Render.com](https://render.com) → **Sign up with GitHub**
- [ ] Créer un compte sur [Vercel.com](https://vercel.com) → **Continue with GitHub**

---

# ÉTAPE 1 : Backend sur Render (≈ 15 min)

## 1.1 Base de données

1. Va sur [dashboard.render.com](https://dashboard.render.com)
2. **New +** → **PostgreSQL**
3. Remplis :
   - **Name** : `portfolio-db`
   - **Region** : Frankfurt (ou la plus proche)
   - **Plan** : Free
4. Clique **Create Database**
5. **IMPORTANT** : Copie l’**Internal Database URL** (bouton "Copy") et garde-la de côté

## 1.2 Service web (backend Django)

1. Toujours sur Render : **New +** → **Web Service**
2. Connecte GitHub si demandé, puis choisis le repo **Mocey2/ANGULAR_PORTFOLIO**
3. Remplis :

| Champ | Valeur |
|-------|--------|
| **Name** | `portfolio-backend` |
| **Region** | Même que la BDD (ex. Frankfurt) |
| **Root Directory** | `portfolio-backend` |
| **Runtime** | Python 3 |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT` |

4. Section **Environment** → **Add Environment Variable** :

| Key | Value |
|-----|-------|
| `DATABASE_URL` | Colle l’Internal Database URL copiée à l’étape 1.1 |
| `SECRET_KEY` | Clique sur **Generate** (Render génère une clé) |
| `DEBUG` | `False` |
| `FRONTEND_URL` | `https://placeholder.vercel.app` (on changera après) |
| `WEB_CONCURRENCY` | `2` |

5. **Plan** : Free
6. Clique **Create Web Service**

## 1.3 Attendre le déploiement

Le premier déploiement prend 5 à 10 minutes. Surveille les logs (bouton "Logs").

Quand c’est vert ✅, note l’URL du backend, par ex. :  
**https://portfolio-backend-xxxx.onrender.com**

## 1.4 Créer ton compte admin

1. Dans ton service backend Render → onglet **Shell**
2. Tape :
```bash
python manage.py createsuperuser
```
3. Entre un **username**, **email** et **mot de passe** (pour l’admin Django)

## 1.5 Charger les données (optionnel)

Dans le même Shell :
```bash
python manage.py load_initial_data
```

---

# ÉTAPE 2 : Frontend sur Vercel (≈ 10 min)

## 2.1 Mettre l’URL du backend dans le code

1. Ouvre `portfolio-angular/src/environments/environment.prod.ts`
2. Remplace `TON-BACKEND-RENDER` par l’URL de ton backend **sans** `https://` ni `/api`
   - Exemple : si ton backend est `https://portfolio-backend-abc1.onrender.com`
   - Mets : `apiUrl: 'https://portfolio-backend-abc1.onrender.com/api',`
3. Sauvegarde, puis dans le terminal :
```powershell
cd C:\Users\Oceane\Desktop\ANGULAR
git add .
git commit -m "Config API backend pour production"
git push
```

## 2.2 Déployer sur Vercel

1. Va sur [vercel.com](https://vercel.com) et connecte-toi avec GitHub
2. **Add New** → **Project**
3. Sélectionne le repo **ANGULAR_PORTFOLIO**
4. Remplis :

| Champ | Valeur |
|-------|--------|
| **Framework Preset** | Other |
| **Root Directory** | `portfolio-angular` (clique Edit et choisis ce dossier) |
| **Build Command** | `npm run build` |
| **Output Directory** | `dist/portfolio/browser` |
| **Install Command** | `npm install` |

5. Clique **Deploy**
6. Attends 2 à 5 minutes
7. **Note l’URL** du frontend, ex. : **https://angular-portfolio-xxxx.vercel.app**

## 2.3 Mettre à jour le CORS côté backend

1. Retourne sur [Render](https://dashboard.render.com) → ton service **portfolio-backend**
2. Onglet **Environment**
3. Modifie `FRONTEND_URL` : remplace `https://placeholder.vercel.app` par l’URL Vercel réelle (ex. `https://angular-portfolio-xxxx.vercel.app`)
4. **Save Changes** (Render redéploiera automatiquement)

---

# ÉTAPE 3 : Vérifier

- [ ] **Site** : Ouvre l’URL Vercel → ton portfolio s’affiche
- [ ] **Admin** : Ouvre `https://TON-BACKEND.onrender.com/admin/` → connecte-toi avec le superuser
- [ ] **Contact** : Teste le formulaire de contact

---

## Tes URLs finales

- **Frontend (site)** : `https://[ton-projet].vercel.app`
- **Backend (admin)** : `https://portfolio-backend-xxxx.onrender.com/admin/`
- **API** : `https://portfolio-backend-xxxx.onrender.com/api/`

---

## En cas de problème

- **Page blanche** : Vérifie que `environment.prod.ts` pointe vers le bon backend
- **Erreur CORS** : Vérifie que `FRONTEND_URL` sur Render = URL Vercel exacte (sans slash final)
- **Backend lent** : Normal au premier chargement (plan gratuit = veille après 15 min d’inactivité)
