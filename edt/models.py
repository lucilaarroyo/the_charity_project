from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
from django import forms

author = 'Your name here'

doc = """
edt
"""


class Constants(BaseConstants):
    name_in_url = 'edt'

    players_per_group = None

    num_adv_rounds = 15
    round_multiplier = 3
    num_rounds = num_adv_rounds * round_multiplier

    level = ['Easy', 'Hard']

    num_dots_easy = [17, 23]
    # num_dots_medium = [18, 22]
    num_dots_hard = [19, 21]

    dots_secs = 1.5


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['extra_dots_displayed'] = []



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    difficulty = models.StringField()
    num_of_dots = models.IntegerField()
    decision = models.IntegerField(choices=[17, 19, 21, 23])
    correct_decision = models.BooleanField()
    num_extra_rounds = models.IntegerField()

