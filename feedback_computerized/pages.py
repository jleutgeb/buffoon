from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        players = self.group.get_players()
        for p in players:
            rounds_in_buffoon = p.session.vars['num_rounds_computerized']
            pot = p.session.vars['pot_buffoon_computerized']
            paid_param_set = random.randint(0, rounds_in_buffoon - 1)
            p.paid_round = p.participant.vars['order_computerized'].index(paid_param_set) + 1

            if p.role() == 'A':
                p.A_attack_B = p.participant.vars['choices_computerized'][paid_param_set][0]
                p.B_attack_C = p.session.vars['npc_actions_computerized'][paid_param_set][1]
                p.C_attack_A = p.session.vars['npc_actions_computerized'][paid_param_set][2]

            if p.role() == 'B':
                p.A_attack_B = p.session.vars['npc_actions_computerized'][paid_param_set][0]
                p.B_attack_C = p.participant.vars['choices_computerized'][paid_param_set][0]
                p.C_attack_A = p.session.vars['npc_actions_computerized'][paid_param_set][2]

            if p.role() == 'C':
                p.A_attack_B = p.session.vars['npc_actions_computerized'][paid_param_set][0]
                p.B_attack_C = p.session.vars['npc_actions_computerized'][paid_param_set][1]
                p.C_attack_A = p.participant.vars['choices_computerized'][paid_param_set][0]

            p.piA = p.session.vars['pis_betas_computerized'][paid_param_set][0]
            p.piB = p.session.vars['pis_betas_computerized'][paid_param_set][1]
            p.piC = p.session.vars['pis_betas_computerized'][paid_param_set][2]
            p.betaA = p.session.vars['pis_betas_computerized'][paid_param_set][3]
            p.betaB = p.session.vars['pis_betas_computerized'][paid_param_set][4]
            p.betaC = p.session.vars['pis_betas_computerized'][paid_param_set][5]

            # draw hits and implosions
            p.A_chance_hit = random.random()
            p.B_chance_hit = random.random()
            p.C_chance_hit = random.random()
            p.A_chance_implode = random.random()
            p.B_chance_implode = random.random()
            p.C_chance_implode = random.random()

            p.A_hits = 0
            p.B_hits = 0
            p.C_hits = 0
            p.A_implodes = 0
            p.B_implodes = 0
            p.C_implodes = 0

            if p.A_chance_hit < p.piA:
                p.A_hits = 1
            if p.B_chance_hit < p.piB:
                p.B_hits = 1
            if p.C_chance_hit < p.piC:
                p.C_hits = 1
            if p.A_chance_implode < p.betaA:
                p.A_implodes = 1
            if p.B_chance_implode < p.betaB:
                p.B_implodes = 1
            if p.C_chance_implode < p.betaC:
                p.C_implodes = 1

            p.A_survives = 1
            p.B_survives = 1
            p.C_survives = 1

            if p.A_implodes == 1 or (p.B_attack_C == 0 and p.B_hits == 1) or (
                    p.C_attack_A == 1 and p.C_hits == 1):
                p.A_survives = 0
            if p.B_implodes == 1 or (p.A_attack_B == 1 and p.A_hits == 1) or (
                    p.C_attack_A == 0 and p.C_hits == 1):
                p.B_survives = 0
            if p.C_implodes == 1 or (p.A_attack_B == 0 and p.A_hits == 1) or (
                    p.B_attack_C == 1 and p.B_hits == 1):
                p.C_survives = 0

            p.num_survivors = p.A_survives + p.B_survives + p.C_survives

            if p.A_survives == 1 and p.role() == 'A':
                p.payoff = pot / p.num_survivors
            if p.B_survives == 1 and p.role() == 'B':
                p.payoff = pot / p.num_survivors
            if p.C_survives == 1 and p.role() == 'C':
                p.payoff = pot / p.num_survivors


class Results(Page):
    def vars_for_template(self):
        highlight = []
        you_survive = []
        if self.player.role() == 'A':
            highlight = 2
            you_survive = self.player.A_survives
        if self.player.role() == 'B':
            highlight = 3
            you_survive = self.player.B_survives
        if self.player.role() == 'C':
            highlight = 4
            you_survive = self.player.C_survives
        payoffA = c(0)
        payoffB = c(0)
        payoffC = c(0)

        if self.player.A_survives == 1:
            payoffA = self.session.vars['pot_buffoon_computerized'] / self.player.num_survivors
        if self.player.B_survives == 1:
            payoffB = self.session.vars['pot_buffoon_computerized'] / self.player.num_survivors
        if self.player.C_survives == 1:
            payoffC = self.session.vars['pot_buffoon_computerized'] / self.player.num_survivors

        return {'highlight': highlight,
                'choice': int(0),
                'you_survive': you_survive,
                'pot': self.session.vars['pot_buffoon_computerized'],
                'payoffA': payoffA,
                'payoffB': payoffB,
                'payoffC': payoffC,
                'piA': int(self.player.piA * 100),
                'piB': int(self.player.piB * 100),
                'piC': int(self.player.piC * 100),
                'betaA': int(self.player.betaA * 100),
                'betaB': int(self.player.betaB * 100),
                'betaC': int(self.player.betaC * 100),
                'A_attack_B': self.player.A_attack_B,
                'B_attack_C': self.player.B_attack_C,
                'C_attack_A': self.player.C_attack_A,
                'A_hits': self.player.A_hits,
                'B_hits': self.player.B_hits,
                'C_hits': self.player.C_hits,
                'A_implodes': self.player.A_implodes,
                'B_implodes': self.player.B_implodes,
                'C_implodes': self.player.C_implodes,
                'A_survives': self.player.A_survives,
                'B_survives': self.player.B_survives,
                'C_survives': self.player.C_survives,
                'num_survivors': self.player.num_survivors,
                'paid_round': self.player.paid_round,
                'role': self.player.role(),
                }


page_sequence = [ResultsWaitPage, Results]
