from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'feedback_computerized'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        rounds_in_buffoon = self.session.vars['num_rounds_computerized']
        paid_param_set = random.randint(0, rounds_in_buffoon - 1)
        players = self.get_players()
        for p in players:
            p.paid_round = p.participant.vars['order_computerized'].index(paid_param_set) + 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    paid_round = models.IntegerField()
    A_attack_B = models.BooleanField()
    B_attack_C = models.BooleanField()
    C_attack_A = models.BooleanField()
    piA = models.FloatField()
    piB = models.FloatField()
    piC = models.FloatField()
    betaA = models.FloatField()
    betaB = models.FloatField()
    betaC = models.FloatField()
    A_hits = models.BooleanField()
    B_hits = models.BooleanField()
    C_hits = models.BooleanField()
    A_implodes = models.BooleanField()
    B_implodes = models.BooleanField()
    C_implodes = models.BooleanField()
    A_survives = models.BooleanField()
    B_survives = models.BooleanField()
    C_survives = models.BooleanField()
    A_chance_hit = models.FloatField()
    B_chance_hit = models.FloatField()
    C_chance_hit = models.FloatField()
    A_chance_implode = models.FloatField()
    B_chance_implode = models.FloatField()
    C_chance_implode = models.FloatField()
    num_survivors = models.IntegerField()

    def role(self):
        paid_param_set = self.paid_round - 1
        return self.session.vars['player_roles_computerized'][paid_param_set]
