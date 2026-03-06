# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_profile_cv_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='personality',
            field=models.TextField(blank=True, help_text="Personnalité : jovialité, leadership, aide aux autres..."),
        ),
    ]
