from django.db import models


class Profile(models.Model):
    """Profil principal du portfolio (un seul enregistrement)."""
    full_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100, blank=True, help_text="Ex: Océane")
    last_name = models.CharField(max_length=100, blank=True, help_text="Ex: Konan")
    headline = models.CharField(max_length=200, blank=True)
    bio_lead = models.TextField(help_text="Texte d'accroche (ex: Dynamique et déterminée)")
    bio_paragraph = models.TextField(help_text="Paragraphe de présentation")
    personality = models.TextField(blank=True, help_text="Personnalité : jovialité, leadership, aide aux autres...")
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='profile/', blank=True, null=True, help_text='CV au format PDF')
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.full_name


class Education(models.Model):
    """Formations."""
    period = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Experience(models.Model):
    """Expériences, certificats, hackathons."""
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Compétences techniques."""
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Interest(models.Model):
    """Centres d'intérêt."""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=50, default='fas fa-star')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Project(models.Model):
    """Projets du portfolio."""
    class TypeChoices(models.TextChoices):
        ACADEMIQUE = 'academique', 'Académique'
        PERSONNEL = 'personnel', 'Personnel'

    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=300)
    full_desc = models.TextField()
    tech = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_type = models.CharField(max_length=20, choices=TypeChoices.choices)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Fact(models.Model):
    """Chiffres clés (formations, projets, etc.)."""
    number = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, blank=True, default='+')
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default='fas fa-star')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.number}{self.suffix} {self.label}"


class ContactMessage(models.Model):
    """Messages du formulaire de contact."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.email}"
