from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.attacks()


class Results(Page):
    def vars_for_template(self):
        highlight = []
        you_survive = 2
        if self.player.role() == 'A':
            highlight = 2
            you_survive = self.group.A_survives
        if self.player.role() == 'B':
            highlight = 3
            you_survive = self.group.B_survives
        if self.player.role() == 'C':
            highlight = 4
            you_survive = self.group.C_survives
        return {'highlight': highlight,
                'choice': int(0),
                'you_survive': you_survive,
                'pot': self.session.vars['pot_buffoon'],
                'payoffA': self.group.get_player_by_role('A').payoff,
                'payoffB': self.group.get_player_by_role('B').payoff,
                'payoffC': self.group.get_player_by_role('C').payoff,
                'piA': int(self.group.piA * 100),
                'piB': int(self.group.piB * 100),
                'piC': int(self.group.piC * 100),
                'betaA': int(self.group.betaA * 100),
                'betaB': int(self.group.betaB * 100),
                'betaC': int(self.group.betaC * 100),
                'A_attack_B': self.group.A_attack_B,
                'B_attack_C': self.group.B_attack_C,
                'C_attack_A': self.group.C_attack_A,
                'A_hits': self.group.A_hits,
                'B_hits': self.group.B_hits,
                'C_hits': self.group.C_hits,
                'A_implodes': self.group.A_implodes,
                'B_implodes': self.group.B_implodes,
                'C_implodes': self.group.C_implodes,
                'A_survives': self.group.A_survives,
                'B_survives': self.group.B_survives,
                'C_survives': self.group.C_survives,
                'num_survivors': self.group.num_survivors,
                'paid_round': self.player.paid_round,
                'role': self.player.role(),
                }


page_sequence = [ResultsWaitPage, Results]
