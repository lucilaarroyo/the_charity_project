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

    num_charities = 60
    num_trial_rounds = 10
    num_rounds = num_trial_rounds + num_charities

    roles = ['Advisor', 'Decider']

    num_dots_easy = [17,23]
    num_dots_medium = [18, 22]
    num_dots_hard = [19, 21]



class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1 or self.round_number == (Constants.num_trial_rounds + 1):
            self.group_randomly()

        elif 1 < self.round_number < (Constants.num_trial_rounds + 1):
            self.group_like_round(1)

        else:
            self.group_like_round(Constants.num_trial_rounds + 1)

        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['m_l'] = []
                p.participant.vars['m_t'] = []
                if p.id_in_group == 1:
                    p.participant.vars['role_1'] = Constants.roles[0]
                    p.participant.vars['role_2'] = Constants.roles[1]
                else:
                    p.participant.vars['role_1'] = Constants.roles[1]
                    p.participant.vars['role_2'] = Constants.roles[0]

        if self.round_number == (Constants.num_trial_rounds + 1):
            for group in self.get_groups():
                group.get_player_by_id(1).participant.vars['role_3'] = random.choice(Constants.roles)
                if group.get_player_by_id(1).participant.vars['role_3'] == Constants.roles[0]:
                    group.get_player_by_id(2).participant.vars['role_3'] = Constants.roles[1]
                else:
                    group.get_player_by_id(2).participant.vars['role_3'] = Constants.roles[0]

        if self.round_number == 1:
            for g in self.get_groups():
                #need to change if num_trial_rounds changes
                dots_displayed_trial_1 = [random.choice(Constants.num_dots_easy)] + [random.choice(Constants.num_dots_medium)] \
                                        + random.choices(Constants.num_dots_hard, k=3)
                random.shuffle(dots_displayed_trial_1)
                dots_displayed_trial_2 = [random.choice(Constants.num_dots_easy)] + [random.choice(Constants.num_dots_medium)] \
                                         + random.choices(Constants.num_dots_hard, k=3)
                random.shuffle(dots_displayed_trial_2)
                dots_displayed_trial = dots_displayed_trial_1 + dots_displayed_trial_2
                for player in g.get_players():
                    player.participant.vars['dots_displayed_trial'] = dots_displayed_trial

        if self.round_number == (Constants.num_trial_rounds + 1):
            for g in self.get_groups():
                dots_displayed = random.choices(Constants.num_dots_easy, k=10) + random.choices(Constants.num_dots_medium, k=10) \
                                 + random.choices(Constants.num_dots_hard, k=40)
                random.shuffle(dots_displayed)
                for player in g.get_players():
                    player.participant.vars['dots_displayed'] = dots_displayed






class Group(BaseGroup):
    pass


class Player(BasePlayer):
    role_in_round = models.StringField()
    num_of_dots = models.IntegerField()
    advice = models.StringField(choices=['LESS', 'MORE'])
    decision = models.StringField(choices=['LESS', 'MORE'])

