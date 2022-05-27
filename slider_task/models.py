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

    slider_value = 1


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
    # S6 = models.IntegerField(blank=True)
    # S7 = models.IntegerField(blank=True)
    # S8 = models.IntegerField(blank=True)
    # S9 = models.IntegerField(blank=True)
    # S10 = models.IntegerField(blank=True)

    charity = models.StringField()
    anonymity = models.StringField()
    donation = models.IntegerField()
    listed = models.StringField()
    total_pub_don = models.IntegerField()
    total_anon_don = models.IntegerField()

    matched_donation = models.StringField()


# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'round_number', 'S1', 'S2', 'S3', 'S4', 'S5',
#            'charity', 'anonymity', 'donation', 'matched_donation']
#     for p in players:
#         yield [p.participant.code, p.round_number, p.S1, p.S2, p.S3, p.S4, p.S5,
#                p.charity, p.anonymity, p.donation, p.matched_donation]


# def custom_export(players):
#     # Title row
#     yield ['round_number',  'listed', 'part_label']
#     for p in players:
#         yield [p.round_number,  p.listed, p.participant.label]