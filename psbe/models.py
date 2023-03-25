from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
from django import forms

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'psbe'
    players_per_group = 2
    num_rounds = 6

    SubC_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
                "item item-7", "item item-8", "item item-9", "item item-10"]
    sca_num = ["item item-0", "item item-1"]

    SCA = ['SCA1', 'SCA2', 'SCA3', 'SCA4', 'SCA5']

    roles = ['Advisor', 'Decider']



class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['orderSubC'] = random.sample(Constants.SubC_num, 10)
                p.participant.vars['orderSCA1'] = random.sample(Constants.sca_num, 2)
                p.participant.vars['orderSCA2'] = random.sample(Constants.sca_num, 2)
                p.participant.vars['orderSCA3'] = random.sample(Constants.sca_num, 2)
                p.participant.vars['orderSCA4'] = random.sample(Constants.sca_num, 2)
                p.participant.vars['orderSCA5'] = random.sample(Constants.sca_num, 2)
                p.participant.vars['orderSCA1to5'] = random.sample(Constants.SCA, 5)
                order_sca6 = random.randint(0, 1)
                if order_sca6 == 0:
                    p.participant.vars['orderSCApages'] = ['SCA6'] + p.participant.vars['orderSCA1to5']
                else:
                    p.participant.vars['orderSCApages'] = p.participant.vars['orderSCA1to5'] + ['SCA6']

                p.participant.vars['end_experiment'] = False

            for group in self.get_groups():
                group.get_player_by_id(1).participant.vars['role'] = random.choice(Constants.roles)
                if group.get_player_by_id(1).participant.vars['role'] == Constants.roles[0]:
                    group.get_player_by_id(2).participant.vars['role'] = Constants.roles[1]
                else:
                    group.get_player_by_id(2).participant.vars['role'] = Constants.roles[0]
                for player in group.get_players():
                    player.rolee = player.participant.vars['role']



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    SIS = models.IntegerField()
    future = models.IntegerField()
    email = models.StringField(blank=True)

    # DEM
    gender = models.StringField(choices=['Female', 'Male', 'Non-binary', 'Other', 'Rather not say'],
                                verbose_name='Which gender do you identify with the most?',
                                widget=widgets.RadioSelect, )
    age = models.IntegerField(verbose_name='What is your age? (Leave blank if you rather not say)', min=18, max=75,
                              blank=True)
    ethnicity = models.StringField(choices=['Hispanic or Latino', 'Non Hispanic or Latino', 'Rather not say'],
                                   verbose_name='Which ethnicity would you describe yourself as?',
                                   widget=widgets.RadioSelect)
    race = models.StringField(choices=['American Indian/Alaska Native', 'Asian', 'Black or African American',
                                       'Native Hawaiian or Other Pacific Islander', 'White', 'Two or More',
                                       'Rather not say'],
                              verbose_name='Which racial category would you describe yourself as?',
                              widget=widgets.RadioSelect)

    # SubC
    SubC1 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC2 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC3 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC4 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC5 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC6 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC7 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC8 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC9 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))
    SubC10 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal(attrs={'class': 'subc'}))

    # TOSCA
    sh1 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh2 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh3 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh4 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh5 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh6 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh7 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh8 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh9 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh10 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    sh11 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())

    g1 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g2 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g3 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g4 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g5 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g6 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g7 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g8 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g9 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g10 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    g11 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())

    d1 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d2 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d3 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d4 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d5 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d6 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d7 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d8 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d9 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d10 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    d11 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())

    e1 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e2 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e3 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e4 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e5 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e6 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e7 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e8 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e9 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e10 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())
    e11 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal())

    rolee = models.StringField()

