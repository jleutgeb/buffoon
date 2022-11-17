from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Info

        yield pages.Choice, dict(
            A_attack_B=random.randint(0, 1),
            B_attack_C=random.randint(0, 1),
            C_attack_A=random.randint(0, 1),
        )
