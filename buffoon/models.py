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


author = 'Johannes Leutgeb'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'buffoon'
    players_per_group = None
    num_rounds = 4
    pis_betas = [
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.0],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.25],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.7],
        [0.5, 0.8, 0.6, 0.0, 0.0, 0.7],
    ]
    pot = c(15)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['pot_buffoon'] = Constants.pot
            self.session.vars['num_rounds'] = Constants.num_rounds
            self.session.vars['pis_betas'] = Constants.pis_betas.copy()
            players = self.get_players()
            dummychoices = [[2, 2, 2]]*Constants.num_rounds
            for p in players:
                order = list(range(Constants.num_rounds))
                random.shuffle(order)
                p.participant.vars['order'] = order
                p.participant.vars['choices'] = dummychoices
        else:
            pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    piA = models.FloatField()
    piB = models.FloatField()
    piC = models.FloatField()
    betaA = models.FloatField()
    betaB = models.FloatField()
    betaC = models.FloatField()
    paramSet = models.IntegerField()
    A_attack_B = models.BooleanField(
        choices=[[1, 'B'], [0, 'C']],
        widget=widgets.RadioSelect
    )
    B_attack_C = models.BooleanField(
        choices=[[1, 'C'], [0, 'A']],
        widget=widgets.RadioSelect
    )
    C_attack_A = models.BooleanField(
        choices=[[1, 'A'], [0, 'B']],
        widget=widgets.RadioSelect
    )

    def assign_parameters(self):
        # first, get current round. then check which parameter set is
        cur_round = self.round_number
        param_num = self.participant.vars['order'][cur_round-1]

        # then assign pis and betas and save parameterID in a field
        self.piA = Constants.pis_betas[param_num][0]
        self.piB = Constants.pis_betas[param_num][1]
        self.piC = Constants.pis_betas[param_num][2]
        self.betaA = Constants.pis_betas[param_num][3]
        self.betaB = Constants.pis_betas[param_num][4]
        self.betaC = Constants.pis_betas[param_num][5]
        self.paramSet = param_num
