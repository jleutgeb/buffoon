from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
            'payoff': participant.payoff,
            'participation_fee': self.session.config['participation_fee'],
            'payoff_total': participant.payoff_plus_participation_fee(),
        }


page_sequence = [PaymentInfo]
