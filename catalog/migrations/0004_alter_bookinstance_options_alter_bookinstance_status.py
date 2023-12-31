# Generated by Django 4.2.7 on 2023-12-31 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_options_bookinstance_borrower_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved'), ('m', 'Maintenance')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
