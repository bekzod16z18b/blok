# Generated by Django 4.1.3 on 2022-12-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sotix', models.CharField(max_length=128, verbose_name='Sotix')),
                ('maslahat', models.CharField(choices=[('maslahat', 'In-Vitro, Tomorqa xizmati, Rubikon water')], max_length=128, verbose_name='Mahsulot turi')),
                ('mahsulot_turi', models.CharField(choices=[('kartoshka', 'Kartoshka'), ('sabzi', 'Sabzi'), ('piyoz', 'Piyoz'), ('sarimsoq', 'Sarimsoq'), ('karam', 'Karam'), ('pomidor', 'Pomidor'), ('bodring', 'Bodring'), ('mosh', 'Mosh'), ('loviya', 'Loviya'), ('qovun', 'Qovun'), ('tarvuz', 'Tarvuz'), ('oshqovoq', 'Oshqovoq'), ('olma', 'Olma'), ('o`rik', 'O`rik'), ('xurmo', 'Xurmo'), ('gilos', 'Gilos'), ('anor', 'Anor'), ('limon', 'Limon'), ('nok', 'Nok'), ('uzum', 'Uzum')], max_length=128, verbose_name='Mahsulot turi')),
                ('xarajat', models.IntegerField()),
                ('hosildorlik', models.CharField(max_length=15, verbose_name='Hosildorlik')),
                ('daromad', models.IntegerField()),
            ],
        ),
    ]
