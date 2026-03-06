# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='profile/', help_text='CV au format PDF'),
        ),
    ]
