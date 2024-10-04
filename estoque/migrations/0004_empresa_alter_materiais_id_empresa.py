# Generated by Django 5.1.1 on 2024-10-03 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_alter_materiais_id_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nome_empresa', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='materiais',
            name='id_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.empresa'),
        ),
    ]
