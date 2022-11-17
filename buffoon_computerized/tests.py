from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Info

        if self.player.role() == 'A':
            yield (pages.Choice, {
                'A_attack_B': random.randint(0, 1),
            })

        if self.player.role() == 'B':
            yield (pages.Choice, {
                'B_attack_C': random.randint(0, 1),
            })

        if self.player.role() == 'C':
            yield (pages.Choice, {
                'C_attack_A': random.randint(0, 1),
            })
