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
    name_in_url = 'feedback'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
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

    def attacks(self):
        rounds_in_buffoon = self.session.vars['num_rounds']
        pot = self.session.vars['pot_buffoon']
        paid_param_set = random.randint(0, rounds_in_buffoon - 1)
        players = self.get_players()
        for p in players:
            p.paid_round = p.participant.vars['order'].index(paid_param_set) + 1

        playerA = self.get_player_by_role('A')
        playerB = self.get_player_by_role('B')
        playerC = self.get_player_by_role('C')

        self.A_attack_B = playerA.participant.vars['choices'][paid_param_set][0]
        self.B_attack_C = playerB.participant.vars['choices'][paid_param_set][1]
        self.C_attack_A = playerC.participant.vars['choices'][paid_param_set][2]

        self.piA = self.session.vars['pis_betas'][paid_param_set][0]
        self.piB = self.session.vars['pis_betas'][paid_param_set][1]
        self.piC = self.session.vars['pis_betas'][paid_param_set][2]
        self.betaA = self.session.vars['pis_betas'][paid_param_set][3]
        self.betaB = self.session.vars['pis_betas'][paid_param_set][4]
        self.betaC = self.session.vars['pis_betas'][paid_param_set][5]

        # draw hits and implosions
        self.A_chance_hit = random.random()
        self.B_chance_hit = random.random()
        self.C_chance_hit = random.random()
        self.A_chance_implode = random.random()
        self.B_chance_implode = random.random()
        self.C_chance_implode = random.random()

        self.A_hits = 0
        self.B_hits = 0
        self.C_hits = 0
        self.A_implodes = 0
        self.B_implodes = 0
        self.C_implodes = 0

        if self.A_chance_hit < self.piA:
            self.A_hits = 1
        if self.B_chance_hit < self.piB:
            self.B_hits = 1
        if self.C_chance_hit < self.piC:
            self.C_hits = 1
        if self.A_chance_implode < self.betaA:
            self.A_implodes = 1
        if self.B_chance_implode < self.betaB:
            self.B_implodes = 1
        if self.C_chance_implode < self.betaC:
            self.C_implodes = 1

        self.A_survives = 1
        self.B_survives = 1
        self.C_survives = 1

        if self.A_implodes == 1 or (self.B_attack_C == 0 and self.B_hits == 1) or (self.C_attack_A == 1 and self.C_hits == 1):
            self.A_survives = 0
        if self.B_implodes == 1 or (self.A_attack_B == 1 and self.A_hits == 1) or (self.C_attack_A == 0 and self.C_hits == 1):
            self.B_survives = 0
        if self.C_implodes == 1 or (self.A_attack_B == 0 and self.A_hits == 1) or (self.B_attack_C == 1 and self.B_hits == 1):
            self.C_survives = 0

        self.num_survivors = self.A_survives + self.B_survives + self.C_survives

        if self.A_survives == 1:
            playerA.payoff = pot/self.num_survivors
        if self.B_survives == 1:
            playerB.payoff = pot/self.num_survivors
        if self.C_survives == 1:
            playerC.payoff = pot/self.num_survivors


class Player(BasePlayer):
    paid_round = models.IntegerField()

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        if self.id_in_group == 2:
            return 'B'
        if self.id_in_group == 3:
            return 'C'

