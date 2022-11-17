from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Assignment(WaitPage):
    # assign the parameter set for the current round
    def after_all_players_arrive(self):
        players = self.group.get_players()
        # gather npc actions from Constants
        for p in players:
            p.assign_parameters()


class Info(Page):
    def is_displayed(self):
        return self.round_number == 1


class Choice(Page):
    form_model = 'player'

    def get_form_fields(self):
        field = []
        if self.player.role() == 'A':
            field = ['A_attack_B']
        if self.player.role() == 'B':
            field = ['B_attack_C']
        if self.player.role() == 'C':
            field = ['C_attack_A']
        return field

    def vars_for_template(self):
        if self.player.role() == 'A':
            return {'param': int(self.player.paramSet),
                    'piA': int(self.player.piA * 100),
                    'piB': int(self.player.piB * 100),
                    'piC': int(self.player.piC * 100),
                    'betaA': int(self.player.betaA * 100),
                    'betaB': int(self.player.betaB * 100),
                    'betaC': int(self.player.betaC * 100),
                    'choice': int(1),
                    'B_attack_C': self.player.B_attack_C,
                    'C_attack_A': self.player.C_attack_A
                    }
        if self.player.role() == 'B':
            return {'param': int(self.player.paramSet),
                    'piA': int(self.player.piA * 100),
                    'piB': int(self.player.piB * 100),
                    'piC': int(self.player.piC * 100),
                    'betaA': int(self.player.betaA * 100),
                    'betaB': int(self.player.betaB * 100),
                    'betaC': int(self.player.betaC * 100),
                    'choice': int(1),
                    'A_attack_B': self.player.A_attack_B,
                    'C_attack_A': self.player.C_attack_A
                    }
        if self.player.role() == 'C':
            return {'param': int(self.player.paramSet),
                    'piA': int(self.player.piA * 100),
                    'piB': int(self.player.piB * 100),
                    'piC': int(self.player.piC * 100),
                    'betaA': int(self.player.betaA * 100),
                    'betaB': int(self.player.betaB * 100),
                    'betaC': int(self.player.betaC * 100),
                    'choice': int(1),
                    'A_attack_B': self.player.A_attack_B,
                    'B_attack_C': self.player.B_attack_C
                    }

    def before_next_page(self):
        choice = []
        if self.player.role() == 'A':
            choice = [self.player.A_attack_B]
        if self.player.role() == 'B':
            choice = [self.player.B_attack_C]
        if self.player.role() == 'C':
            choice = [self.player.C_attack_A]

        choices = self.player.participant.vars['choices_computerized']
        choices[self.player.paramSet] = choice
        self.player.participant.vars['choices_computerized'] = choices


page_sequence = [Info, Assignment, Choice]
