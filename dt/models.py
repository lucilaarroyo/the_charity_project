from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random



doc = """
dt 

"""


class Constants(BaseConstants):
    name_in_url = 'dt'
    players_per_group = 2
    num_charities = 20
    # num_charities = 3
    num_rounds = num_charities
    charities = ['FACING HUNGER FOODBANK', 'WATER MISSION', 'KIDNEY CANCER ASSOCIATION', 'THE ASSOCIATION FOR FRONTOTEMPORAL DEGENERATION',
                 'THE TREVOR PROJECT', 'THE GLOBAL ORPHAN PROJECT', 'CHRISTIAN RELIEF FUND', 'SBP', 'INTERNATIONAL RELIEF TEAMS',
                 'FISHER HOUSE FOUNDATION', 'BUILDING HOMES FOR HEROES', 'MEMORIAL ASSISTANCE MINISTRIES', 'CHICAGO COALITION FOR THE HOMELESS',
                 'ALIGHT', 'REFUGEES INTERNATIONAL', 'WOMEN IN DISTRESS OF BROWARD COUNTY', 'SAFEHOUSE DENVER', 'JUSTICE IN AGING',
                 'THE DIAN FOSSEY GORILLA FUND INTERNATIONAL', 'RE- WILD']

    max_tasks = 20
    slider_value = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['orderDT'] = random.sample(Constants.charities, Constants.num_charities)
                player.participant.vars['this_round'] = random.randint(1, Constants.num_charities)
                player.participant.vars['chosen_charity'] = []
                player.participant.vars['chosen_tasks_committed'] = []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    STI1 = models.IntegerField()

    def STI1_error_message(self, value):
        if value != 50:
            return 'Please position slider at 50'

    STI2 = models.IntegerField()

    def STI2_error_message(self, value):
        if value != 50:
            return 'Please position slider at 50'

    STT1 = models.IntegerField(blank=True)
    STT2 = models.IntegerField(blank=True)
    STT3 = models.IntegerField(blank=True)
    STT4 = models.IntegerField(blank=True)
    STT5 = models.IntegerField(blank=True)

    CST = models.DecimalField(max_digits=10, decimal_places=2)

    charity = models.StringField()
    tasks_committed = models.IntegerField(min=0, max=Constants.max_tasks)
    chosen_charity = models.StringField()
    chosen_tasks_committed = models.IntegerField()

