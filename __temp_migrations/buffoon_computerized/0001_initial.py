# Generated by Django 2.2.12 on 2022-11-17 09:41

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buffoon_computerized_group', to='otree.Session')),
            ],
            options={
                'db_table': 'buffoon_computerized_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buffoon_computerized_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'buffoon_computerized_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('piA', otree.db.models.FloatField(null=True)),
                ('piB', otree.db.models.FloatField(null=True)),
                ('piC', otree.db.models.FloatField(null=True)),
                ('betaA', otree.db.models.FloatField(null=True)),
                ('betaB', otree.db.models.FloatField(null=True)),
                ('betaC', otree.db.models.FloatField(null=True)),
                ('paramSet', otree.db.models.IntegerField(null=True)),
                ('A_attack_B', otree.db.models.BooleanField(choices=[[1, 'B'], [0, 'C']], null=True, verbose_name='Wen greifen Sie an?')),
                ('B_attack_C', otree.db.models.BooleanField(choices=[[1, 'C'], [0, 'A']], null=True, verbose_name='Wen greifen Sie an?')),
                ('C_attack_A', otree.db.models.BooleanField(choices=[[1, 'A'], [0, 'B']], null=True, verbose_name='Wen greifen Sie an?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buffoon_computerized.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buffoon_computerized_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buffoon_computerized_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buffoon_computerized.Subsession')),
            ],
            options={
                'db_table': 'buffoon_computerized_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buffoon_computerized.Subsession'),
        ),
    ]
