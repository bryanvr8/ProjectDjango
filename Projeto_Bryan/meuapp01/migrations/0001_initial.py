# Generated by Django 4.1.7 on 2023-03-31 16:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dados', models.CharField(max_length=60, null=True)),
                ('codigo', models.CharField(max_length=60, null=True)),
                ('descricao', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
