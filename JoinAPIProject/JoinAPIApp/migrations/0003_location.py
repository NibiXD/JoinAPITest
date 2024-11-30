# Generated by Django 4.2.16 on 2024-11-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoinAPIApp', '0002_alter_pessoa_id_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('dataDeExpiracao', models.DateTimeField()),
            ],
            options={
                'db_table': 'location',
            },
        ),
    ]
