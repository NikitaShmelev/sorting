# Generated by Django 3.0.4 on 2020-04-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200409_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorting',
            name='algorithm',
            field=models.CharField(choices=[('Buble', 'Buble'), ('Insertion', 'Insertion'), ('Merge', 'Merge')], default='Buble', max_length=18),
        ),
    ]
