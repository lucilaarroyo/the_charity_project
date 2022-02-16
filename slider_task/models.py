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
slider_task
"""


class Constants(BaseConstants):
    name_in_url = 'slider_task'
    players_per_group = None
    num_rounds = 20

    slider_value = 0.10


class Subsession(BaseSubsession):
    pass
    # def creating_session(self):
    #     if self.round_number == 1:
    #         # randomize
    #         for player in self.get_players():
    #             player.participant.vars['orderWEW1'] = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    S1 = models.IntegerField(blank=True)
    S2 = models.IntegerField(blank=True)
    S3 = models.IntegerField(blank=True)
    S4 = models.IntegerField(blank=True)
    S5 = models.IntegerField(blank=True)
    S6 = models.IntegerField(blank=True)
    S7 = models.IntegerField(blank=True)
    S8 = models.IntegerField(blank=True)
    S9 = models.IntegerField(blank=True)
    S10 = models.IntegerField(blank=True)

    charity = models.StringField()
    anonymity = models.StringField()
    donation = models.DecimalField(max_digits=3, decimal_places=2)
    listed = models.StringField()

    # matched_donation = models.StringField
    consent = models.IntegerField()
    name_consent = models.StringField(blank=True)


# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'round_number', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
#            'charity', 'anonymity', 'donation']
#     for p in players:
#         yield [p.participant.code, p.round_number, p.S1, p.S2, p.S3, p.S4, p.S5, p.S6, p.S7, p.S8, p.S9, p.S10,
#                p.charity, p.anonymity, p.donation]


def custom_export(players):
    # Title row
    yield ['round_number',  'listed', 'consent', 'name_consent']
    for p in players:
        yield [p.round_number,  p.listed, p.consent, p.name_consent]