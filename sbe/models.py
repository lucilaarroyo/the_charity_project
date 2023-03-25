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
    num_dots_medium = [18, 22]
    num_dots_hard = [19, 21]

    dots_secs = 3
    sec_adv_sees = 3
    sec_dec_sees = 1

    adv_rounds = ["With"] * int(num_actual_rounds/2-1) + ["Without"] * int(num_actual_rounds/2-1)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['m_l'] = []
                p.participant.vars['m_t'] = []
                p.participant.vars['num_correct_adv'] = []
                p.participant.vars['num_extra_rounds'] = 0

        if self.round_number == 1:
            for g in self.get_groups():
                #need to change if num_trial_rounds changes
                dots_displayed_trial = [random.choice(Constants.num_dots_easy)] + random.choices(Constants.num_dots_hard, k=2)
                random.shuffle(dots_displayed_trial)
                for player in g.get_players():
                    player.participant.vars['dots_displayed_trial'] = dots_displayed_trial

        if self.round_number == (Constants.num_trial_rounds + 1):
            for g in self.get_groups():
                difficulty = random.choice(Constants.level)
                w_wo_advice = ["Without", "With"] + random.sample(Constants.adv_rounds, (Constants.num_actual_rounds-2))
                if difficulty == 'Easy':
                    dots_displayed_adv = random.choices(Constants.num_dots_easy, k=8) + random.choices(Constants.num_dots_medium, k=5) \
                                 + random.choices(Constants.num_dots_hard, k=2)
                    random.shuffle(dots_displayed_adv)
                    dots_displayed_dec = random.choices(Constants.num_dots_easy, k=8) + random.choices(Constants.num_dots_medium, k=5) \
                                         + random.choices(Constants.num_dots_hard, k=2)
                    random.shuffle(dots_displayed_dec)
                    for_dots_displayed = []
                    for i in w_wo_advice:
                        if i == 'With':
                            for_dots_displayed.append(dots_displayed_adv[0])
                            del dots_displayed_adv[0]
                        else:
                            for_dots_displayed.append(dots_displayed_dec[0])
                            del dots_displayed_dec[0]
                    for player in g.get_players():
                        player.participant.vars['dots_displayed'] = for_dots_displayed
                        player.participant.vars['adv_rounds'] = w_wo_advice
                        player.participant.vars['difficulty'] = 'Easy'
                else:
                    dots_displayed_adv = random.choices(Constants.num_dots_easy, k=2) + random.choices(Constants.num_dots_medium, k=5) \
                                 + random.choices(Constants.num_dots_hard, k=8)
                    random.shuffle(dots_displayed_adv)
                    dots_displayed_dec = random.choices(Constants.num_dots_easy, k=2) + random.choices(Constants.num_dots_medium, k=5) \
                                         + random.choices(Constants.num_dots_hard, k=8)
                    random.shuffle(dots_displayed_dec)
                    for_dots_displayed = []
                    for i in w_wo_advice:
                        if i == 'With':
                            for_dots_displayed.append(dots_displayed_adv[0])
                            del dots_displayed_adv[0]
                        else:
                            for_dots_displayed.append(dots_displayed_dec[0])
                            del dots_displayed_dec[0]
                    for player in g.get_players():
                        player.participant.vars['dots_displayed'] = for_dots_displayed
                        player.participant.vars['adv_rounds'] = w_wo_advice
                        player.participant.vars['difficulty'] = 'Hard'


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rolee = models.StringField()
    difficulty = models.StringField()
    num_of_dots = models.IntegerField()
    advice = models.StringField(choices=['LESS', 'MORE'])
    decision = models.StringField(choices=['LESS', 'MORE'])
    correct_advice = models.BooleanField()
    correct_decision = models.BooleanField()
    correctness = models.BooleanField()
    num_adv_incorrect = models.IntegerField()
    num_extra_rounds = models.IntegerField()
