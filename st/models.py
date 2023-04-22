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


author = 'Your name here'

doc = """
st
"""


class Constants(BaseConstants):
    name_in_url = 'st'
    players_per_group = None
    num_rounds = 20

    slider_value = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['total_don'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    S1 = models.IntegerField(blank=True)
    S2 = models.IntegerField(blank=True)
    S3 = models.IntegerField(blank=True)
    S4 = models.IntegerField(blank=True)
    S5 = models.IntegerField(blank=True)

    charity = models.StringField()
    donation = models.IntegerField()
    total_don = models.IntegerField()