"""Charge les données initiales du portfolio."""
from django.core.management.base import BaseCommand
from portfolio.models import Profile, Education, Experience, Skill, Interest, Project, Fact


class Command(BaseCommand):
    help = 'Charge les données initiales du portfolio'

    def handle(self, *args, **options):
        if Profile.objects.exists():
            self.stdout.write('Les données existent déjà. Supprimez-les avant de réinitialiser.')
            return

        Profile.objects.create(
            full_name='Mahou Grace Océane Konan',
            first_name='Océane',
            last_name='Konan',
            headline='Étudiante en Génie Logiciel',
            bio_lead='Dynamique et déterminée',
            bio_paragraph=(
                "je poursuis mes études en génie logiciel où je développe de solides compétences "
                "en analyse et conception de systèmes informatiques, ainsi qu'en réseaux. "
                "Enthousiaste à l'idée de contribuer à des projets innovants, je souhaite rejoindre "
                "un environnement professionnel qui valorise l'initiative et la créativité technique."
            ),
            email='gracemahouk@gmail.com',
            phone='+225 07 87 25 83 54',
            linkedin_url='https://linkedin.com',
            github_url='https://github.com',
        )

        Education.objects.bulk_create([
            Education(period='Oct 2023 – Présent', title='Licence en Informatique',
                      place='Institut Ivoirien de Technologie, Grand-Bassam', order=1),
            Education(period='Sep 2021 – Jul 2023', title='Baccalauréat Scientifique',
                      place='Collège Méthodiste, Cocody', order=2),
        ])

        Experience.objects.bulk_create([
            Experience(title='Certificat séminaire intelligence artificielle', order=1),
            Experience(title='Participation hackathon', order=2),
            Experience(title="Formation réunissant les développeurs d'application", order=3),
        ])

        skills = ['Django', 'Flutter', 'Python', 'Bases de données', 'HTML, CSS, JS', 'Méthodes Agiles']
        for i, name in enumerate(skills):
            Skill.objects.create(name=name, order=i + 1)

        Interest.objects.bulk_create([
            Interest(title='Photographie & Vidéo', icon='fas fa-camera', order=1),
            Interest(title="Organisation d'événements",
                     icon='fas fa-calendar-alt', order=2),
            Interest(title='Bénévolat culturel', subtitle='Concerts et événements',
                     icon='fas fa-music', order=3),
            Interest(title='Pâtisserie', subtitle='Nouvelles recettes',
                     icon='fas fa-birthday-cake', order=4),
        ])

        projects = [
            {
                'title': "O'MEDICAL", 'short_desc': 'Prise de rendez-vous et consultation en ligne',
                'full_desc': "Application mobile de prise de rendez-vous et consultation médicale en ligne. "
                             "Permet aux patients de réserver des créneaux et de consulter en ligne.",
                'tech': 'Flutter', 'project_type': 'academique', 'order': 1,
            },
            {
                'title': "N'SAPKA", 'short_desc': 'Marketplace artisans et producteurs locaux',
                'full_desc': "Application mobile marketplace mettant en relation artisans et producteurs "
                             "locaux avec leurs clients. Plateforme de vente et mise en avant des créateurs ivoiriens.",
                'tech': 'Flutter', 'project_type': 'academique', 'order': 2,
            },
            {
                'title': "Application gestion d'école", 'short_desc': 'Système de gestion scolaire',
                'full_desc': "Application de gestion pour établissements scolaires : suivi des élèves, emplois du temps, "
                             "notes. Développée avec Visual Studio et base de données SQL. Méthodologie Agiles.",
                'tech': 'Visual Studio, SQL, Méthodes Agiles', 'project_type': 'academique', 'order': 3,
            },
            {
                'title': 'Application flotte automobile', 'short_desc': 'Conception gestion de flotte',
                'full_desc': "Conception d'application de gestion de flotte automobile : suivi des véhicules, maintenance, affectations.",
                'tech': 'Conception', 'project_type': 'academique', 'order': 4,
            },
            {
                'title': 'Projet Odoo', 'short_desc': 'Gestion de parc informatique',
                'full_desc': "Mise en place d'un projet Odoo pour la gestion de parc informatique d'une entreprise.",
                'tech': 'Odoo', 'project_type': 'academique', 'order': 5,
            },
            {
                'title': 'Site e-commerce', 'short_desc': 'Boutique en ligne sécurisée',
                'full_desc': "Développement d'un site web e-commerce sécurisé avec paiement, gestion des produits et blog. "
                             "Projet personnel de développement web.",
                'tech': 'Django, REST API', 'project_type': 'personnel', 'order': 6,
            },
            {
                'title': 'Plateforme sportive', 'short_desc': 'Plateforme dédiée au sport',
                'full_desc': "Plateforme web pour la gestion d'activités sportives, inscriptions et suivi. "
                             "Projet personnel de développement.",
                'tech': 'Django, Web', 'project_type': 'personnel', 'order': 7,
            },
        ]
        for p in projects:
            Project.objects.create(**p)

        Fact.objects.bulk_create([
            Fact(number=2, suffix='+', label='Formations', icon='fas fa-graduation-cap', order=1),
            Fact(number=5, suffix='+', label='Langages', icon='fas fa-code', order=2),
            Fact(number=5, suffix='+', label='Projets réalisés', icon='fas fa-project-diagram', order=3),
            Fact(number=1, suffix='', label='Certificat IA', icon='fas fa-certificate', order=4),
        ])

        self.stdout.write(self.style.SUCCESS('Données initiales chargées avec succès !'))
