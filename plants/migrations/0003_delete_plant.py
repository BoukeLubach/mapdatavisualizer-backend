from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20211005_2150'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Plant',
        ),
    ]
