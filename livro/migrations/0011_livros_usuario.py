# Generated by Django 4.1.3 on 2022-12-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0010_remove_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='usuario',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
