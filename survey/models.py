from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    survey_payoff = c(2)


class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        for p in players:
            p.payoff = Constants.survey_payoff


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(
        choices=[
            ['m', 'Männlich'],
            ['f', 'Weiblich'],
            ['o', 'Andere'],
        ],
        label="Geschlecht"
    )
    age = models.IntegerField(min=0, max=100, label="Wie alt sind Sie?")
    field = models.LongStringField(label="Welches Fach studieren Sie?")
    semesters = models.IntegerField(min=0, max=100, label="Im wievielten Fachsemester studieren Sie?")
    strategy = models.LongStringField(blank=True, label="Bitte beschreiben Sie Ihren Gedankenprozess oder Ihre Strategie im Spiel.")
    comments = models.LongStringField(blank=True, label="Haben Sie noch andere Kommentare oder Fragen zum Spiel?")


