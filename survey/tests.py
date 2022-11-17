from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Survey, {'gender': 'm', 'age': 35, 'field': 'econ', 'semesters': 19, 'strategy': 'I did not think too much about it', 'comments': 'Awesome!'})
