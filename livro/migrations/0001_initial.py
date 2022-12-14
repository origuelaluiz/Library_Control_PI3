# Generated by Django 4.1.3 on 2022-11-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('data_cadastro', models.DateField()),
                ('emprestado', models.BooleanField(default=False)),
                ('usuario_emprestado', models.CharField(max_length=30)),
                ('data_emprestimo', models.DateTimeField()),
                ('data_devolucao', models.DateTimeField()),
                ('tempo_duracao', models.DateField()),
            ],
        ),
    ]
