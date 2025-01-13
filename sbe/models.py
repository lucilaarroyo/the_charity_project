from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
from django import forms

author = 'Your name here'

doc = """
sbe
"""


class Constants(BaseConstants):
    name_in_url = 'sbe'

    players_per_group = 2

    num_trial_rounds = 3
    num_actual_rounds = 30
    num_rounds = num_trial_rounds + num_actual_rounds

    round_multiplier = 3

    roles = ['Advisor', 'Decider']
    level = ['Easy', 'Hard']

    num_dots_easy = [17, 23]
    # num_dots_medium = [18, 22]
    num_dots_hard = [19, 21]

    dots_secs = 1.5
    # sec_adv_sees = 0.5
    # sec_dec_sees = 0.5

    adv_rounds = ["With"] * int(num_actual_rounds/2-1) + ["Without"] * int(num_actual_rounds/2-1)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['role'] = ''
                p.participant.vars['dots_displayed_trial'] = []
                p.participant.vars['dots_displayed'] = []
                p.participant.vars['adv_rounds'] = []
                p.participant.vars['difficulty'] = ''
                p.participant.vars['m_l'] = []
                p.participant.vars['m_t'] = []
                p.participant.vars['num_correct_adv'] = 0
                p.participant.vars['num_extra_rounds'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rolee = models.StringField()
    difficulty = models.StringField()
    num_of_dots = models.IntegerField()
    advice = models.IntegerField(choices=[17, 19, 21, 23])
    decision = models.IntegerField(choices=[17, 19, 21, 23])
    correct_advice = models.BooleanField()
    correct_decision = models.BooleanField()
    correctness = models.BooleanField()
    num_adv_incorrect = models.IntegerField()
    num_extra_rounds = models.IntegerField()

    performance = models.StringField(choices=['Very poor', 'Poor', 'Neutral', 'Good', 'Very Good'], widget=widgets.RadioSelect())
