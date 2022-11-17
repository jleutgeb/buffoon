from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Info(Page):
    def is_displayed(self):
        return self.round_number == 1


class Assignment(WaitPage):
    # wait_for_all_groups = True
    # assign the parameter set for the current round
    def after_all_players_arrive(self):
        players = self.group.get_players()
        for p in players:
            p.assign_parameters()


class Choice(Page):
    form_model = 'player'
    form_fields = ['A_attack_B', 'B_attack_C', 'C_attack_A']

    def vars_for_template(self):
        return {'param': int(self.player.paramSet),
                'piA': int(self.player.piA * 100),
                'piB': int(self.player.piB * 100),
                'piC': int(self.player.piC * 100),
                'betaA': int(self.player.betaA * 100),
                'betaB': int(self.player.betaB * 100),
                'betaC': int(self.player.betaC * 100),
                'choice': int(1)
                }

    def before_next_page(self):
        choices = self.player.participant.vars['choices']
        choices[self.player.paramSet] = [self.player.A_attack_B, self.player.B_attack_C, self.player.C_attack_A]
        self.player.participant.vars['choices'] = choices


page_sequence = [Info, Assignment, Choice]
