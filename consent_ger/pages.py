from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyConsentPage(Page):
    form_model = 'player'
    form_fields = ['player_consents']


class MyConsentWaitPage(WaitPage):
    wait_for_all_groups = True


page_sequence = [
    MyConsentPage,
    MyConsentWaitPage,
]
