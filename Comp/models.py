from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
Submissive Compassion 

"""


class Constants(BaseConstants):
    name_in_url = 'Comp'
    players_per_group = None
    num_charities = 2
    num_rounds = num_charities*2 - 1
    charities = ['ACTION AGAINST HUNGER', 'FEED MY STARVING CHILDREN']
    # ['ACTION AGAINST HUNGER', 'FEED MY STARVING CHILDREN', 'FACING HUNGER FOODBANK', 'THE HUNGER COALITION',
    #  'WATER MISSION', 'MULTIPLE MYELOMA RESEARCH FOUNDATION', 'LIVING BEYOND BREAST CANCER', 'FIGHT COLORECTAL CANCER',
    #  'CURE CHILDHOOD CANCER', 'KIDNEY CANCER ASSOCIATION', 'AIDS UNITED', 'ORGANIZATION FOR AUTISM RESEARCH',
    #  'CAN DO MULTIPLE SCLEROSIS', 'SAN DIEGO CENTER FOR THE BLIND', 'DIABETES FOUNDATION OF MISSISSIPPI',
    #  'THE ASSOCIATION FOR FRONTOTEMPORAL DEGENERATION', 'FISHER CENTER FOR ALZHEIMER`S RESEARCH FOUNDATION',
    #  'THE JED FOUNDATION', 'THE TREVOR PROJECT', 'TRAGEDY ASSISTANCE PROGRAM FOR SURVIVORS', 'THE GLOBAL ORPHAN PROJECT',
    #  'HELP THE HELPLESS', 'PREVENT CHILD ABUSE AMERICA', 'SAVE THE CHILDREN', 'CHRISTIAN RELIEF FUND', 'ALL HANDS AND HEARTS',
    #  'SBP', 'SAMARITAN`S PURSE', 'UNITED METHODIST COMMITTEE ON RELIEF OF GLOBAL MINISTRIES', 'INTERNATIONAL RELIEF TEAMS',
    #  'SEMPER FI & AMERICA`S FUND', 'FISHER HOUSE FOUNDATION', 'SOLDIERS` ANGELS', 'OUR MILITARY KIDS', 'BUILDING HOMES FOR HEROES',
    #  'MEMORIAL ASSISTANCE MINISTRIES', 'TRANSITIONS', 'ROSIE`S PLACE', 'HEALTHCARE FOR THE HOMELESS - HOUSTON',
    #  'CHICAGO COALITION FOR THE HOMELESS', 'ALIGHT', 'REFUGEES INTERNATIONAL', 'PREEMPTIVE LOVE', 'THE TIBET FUND',
    #  'UNITED PALESTINIAN APPEAL', 'WOMEN IN DISTRESS OF BROWARD COUNTY', 'ALTERNATIVES', 'THE FAMILY PLACE', 'SAFEHOUSE DENVER',
    #  'LYDIA`S HOUSE', 'AMERICANS FOR IMMIGRANT JUSTICE', 'JUSTICE IN AGING', 'CAMPHILL VILLAGE KIMBERTON HILLS',
    #  'STATE VOICES', 'RAINIER SCHOLARS', 'ANIMAL DEFENSE LEAGUE OF TEXAS', 'THE DIAN FOSSEY GORILLA FUND INTERNATIONAL',
    #  'MICHIGAN ANTI-CRUELTY SOCIETY', 'CHEETAH CONSERVATION FUND', 'GLOBAL WILDLIFE CONSERVATION']

    # anonymity = public or anonymous
    anonymity = ["PUBLIC"] * int(num_charities/2) + ["ANONYMOUS"] * int(num_charities/2)

    #Compensation per 1/2 hour for 1 1/2 hour of participation
    compensation = c(5) * 3
    # Initial amount allocated to the dictator
    endowment = c(20)
    val_endowment = int(endowment)
    # possibledonations = list(range(val_endowment+1))
    match = ['YES', 'NO']

    #questionnaires
    WEW_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
                "item item-7", "item item-8", "item item-9", "item item-10", "item item-11", "item item-12",
                "item item-13", "item item-14"]
    SubC_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
                "item item-7", "item item-8", "item item-9", "item item-10"]
    SAQ_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
               "item item-7", "item item-8", "item item-9", "item item-10"]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            # randomize
            for player in self.get_players():
                player.participant.vars['orderWEW1'] = random.sample(Constants.WEW_num, 14)
                player.participant.vars['orderWEW2'] = random.sample(Constants.WEW_num, 14)
                player.participant.vars['orderWEW3'] = random.sample(Constants.WEW_num, 14)
                player.participant.vars['orderSubC'] = random.sample(Constants.SubC_num, 10)
                player.participant.vars['orderSAQ'] = random.sample(Constants.SAQ_num, 10)
                player.participant.vars['orderTask1'] = random.sample(Constants.charities, Constants.num_charities)
                player.participant.vars['orderTask2'] = random.sample(Constants.charities, Constants.num_charities)
                #player.participant.vars['dictVersion'] = random.sample(Constants.versions, Constants.num_charities*2)
                player.participant.vars['dictAnonym'] = random.sample(Constants.anonymity, Constants.num_charities)
                player.participant.vars['payRound'] = random.randint(Constants.num_charities, Constants.num_rounds)
                player.participant.vars['matchedDonation'] = random.sample(Constants.match, 1)
                #player.participant.vars['version_1_count'] = 0
                # for_for_don = []
                # for i in range(Constants.num_charities):
                #     n = random.randint(0, Constants.val_endowment)
                #     for_for_don.append(n)
                # player.participant.vars['forcedDonation'] = for_for_don

                # For output file
                # player.participant.vars['OT1'] = player.participant.vars['orderTask1'] + \
                #                                  ['']*(Constants.num_rounds-Constants.num_charities)


class Group(BaseGroup):
    pass

    # def set_payoffs(self):
    #     p1 = self.get_player_by_id(1)
    #     p2 = self.get_player_by_id(2)
    #     p1.payoff = self.kept
    #     p2.payoff = Constants.endowment - self.kept


class Player(BasePlayer):

    deservingness = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                        widget=widgets.RadioSelectHorizontal(attrs={'class': 'deser'}))
    closeness = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                    widget=widgets.RadioSelectHorizontal(attrs={'class': 'close'}))

    donation = models.IntegerField(min=0, max=Constants.val_endowment)

    def set_payoffs(self):
        self.payoff = Constants.endowment - self.donation

    # WEW
    WEW1 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW2 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW3 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW4 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW5 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW6 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW7 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW8 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW9 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW10 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW11 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW12 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW13 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))
    WEW14 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'wew'}))


    #SubC
    SubC1 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC2 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC3 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC4 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC5 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC6 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC7 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC8 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC9 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)
    SubC10 = models.IntegerField(choices=[0, 1, 2, 3, 4], widget=widgets.RadioSelectHorizontal)

    #SAQ
    SAQ1 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ2 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ3 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ4 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ5 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ6 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ7 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ8 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ9 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    SAQ10 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    charity_task_1 = models.StringField()
    charity_task_2 = models.StringField()
    anonymity_task_2 = models.StringField()
    payment_round = models.IntegerField()
    endow_portion = models.CurrencyField()
    total_subject_payoff = models.CurrencyField()
    matched_donation = models.StringField()
    subject_donation = models.IntegerField()
    total_donation = models.IntegerField()
    chosen_charity = models.StringField()
    chosen_anonymity = models.StringField()
    consent = models.StringField(blank=True)
    listed = models.StringField()






def custom_export(players):
    # Title row
    yield ['participant_code', 'gender', 'age', 'round_number', 'OrderTask1', 'deservingness', 'closeness',
           'OrderTask2', 'anonymity', 'donation', 'payoff']
    for p in players:
        yield [p.participant.code,  p.gender,  p.age, p.round_number, p.charity_task_1, p.deservingness, p.closeness,
               p.charity_task_2, p.anonymity_task_2, p.donation, p.payoff]




# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'gender', 'age',
#            'WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11', 'WEW12',
#            'WEW13', 'WEW14',
#            'SubC1', 'SubC2', 'SubC3', 'SubC4', 'SubC5', 'SubC6', 'SubC7', 'SubC8', 'SubC9', 'SubC10',
#            'SAQ1', 'SAQ2', 'SAQ3', 'SAQ4', 'SAQ5', 'SAQ6', 'SAQ7', 'SAQ8', 'SAQ9', 'SAQ10']
#     for p in players:
#         yield [p.participant.code, p.gender, p.age,
#                p.WEW1, p.WEW2, p.WEW3, p.WEW4, p.WEW5, p.WEW6, p.WEW7, p.WEW8, p.WEW9, p.WEW10, p.WEW11, p.WEW12,
#                p.WEW13, p.WEW14,
#                p.SubC1, p.SubC2, p.SubC3, p.SubC4, p.SubC5, p.SubC6, p.SubC7, p.SubC8, p.SubC9, p.SubC10,
#                p.SAQ1, p.SAQ2, p.SAQ3, p.SAQ4, p.SAQ5, p.SAQ6, p.SAQ7, p.SAQ8, p.SAQ9, p.SAQ10]




# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'payment_round', 'participation_fee','actual_payoff', 'total_payoff',
#            'matched_donation', 'actual_subject_donation', 'total_donation', 'charity', 'anonymity']
#     for p in players:
#         yield [p.participant.code, p.payment_round, 7, p.actual_payoff, p.total_payoff,
#                p.matched_donation, p.actual_subject_donation, p.total_donation, p.chosen_charity, p.chosen_anonymity]
