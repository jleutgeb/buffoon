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
    name_in_url = 'buffoon_computerized'
    players_per_group = None
    num_rounds = 8
    # [pi_a, pi_b, pi_c, beta_a, beta_b, beta_c]
    pis_betas = [
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.25],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.25],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.25],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.25],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.7],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.7],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.7],
        [0.5, 0.3, 0.6, 0.0, 0.0, 0.7],
    ]
    # [a_attack_b, b_attack_c, c_attack_a]
    npc_actions = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
    ]
    player_roles = [
        'A',
        'A',
        'A',
        'A',
        'A',
        'A',
        'A',
        'A',
    ]
    pot = c(15)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.session.get_participants()


        if self.round_number == 1:
            self.session.vars['pot_buffoon_computerized'] = Constants.pot
            self.session.vars['pis_betas_computerized'] = Constants.pis_betas.copy()
            self.session.vars['npc_actions_computerized'] = Constants.npc_actions.copy()
            self.session.vars['player_roles_computerized'] = Constants.player_roles.copy()
            self.session.vars['num_rounds_computerized'] = Constants.num_rounds
            players = self.get_players()
            dummychoices = [2]*Constants.num_rounds
            for p in players:
                order = list(range(Constants.num_rounds))
                random.shuffle(order)
                p.participant.vars['order_computerized'] = order
                p.participant.vars['choices_computerized'] = dummychoices


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
        widget=widgets.RadioSelect,
        label="Wen greifen Sie an?"
    )
    B_attack_C = models.BooleanField(
        choices=[[1, 'C'], [0, 'A']],
        widget=widgets.RadioSelect,
        label="Wen greifen Sie an?"
    )
    C_attack_A = models.BooleanField(
        choices=[[1, 'A'], [0, 'B']],
        widget=widgets.RadioSelect,
        label="Wen greifen Sie an?"
    )

    def role(self):
        cur_round = self.round_number
        return Constants.player_roles[cur_round-1]

    def assign_parameters(self):
        # first, get current round. then check which parameter set is
        cur_round = self.round_number
        param_num = self.participant.vars['order_computerized'][cur_round-1]

        # then assign pis and betas and save parameterID in a field
        self.piA = Constants.pis_betas[param_num][0]
        self.piB = Constants.pis_betas[param_num][1]
        self.piC = Constants.pis_betas[param_num][2]
        self.betaA = Constants.pis_betas[param_num][3]
        self.betaB = Constants.pis_betas[param_num][4]
        self.betaC = Constants.pis_betas[param_num][5]
        self.paramSet = param_num

        # set actions for npcs
        npc_actions = Constants.npc_actions[param_num]
        if self.role() != 'A':
            self.A_attack_B = npc_actions[0]
        if self.role() != 'B':
            self.B_attack_C = npc_actions[1]
        if self.role() != 'C':
            self.C_attack_A = npc_actions[2]
