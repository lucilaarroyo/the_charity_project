from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random



doc = """
Comp_sona 

"""


class Constants(BaseConstants):
    name_in_url = 'Comp_sona'
    players_per_group = None
    num_charities = 60
    # num_charities = 4
    num_rounds = num_charities*2 - 1
    charities = ['ACTION AGAINST HUNGER', 'FEED MY STARVING CHILDREN', 'FACING HUNGER FOODBANK', 'THE HUNGER COALITION',
     'WATER MISSION', 'MULTIPLE MYELOMA RESEARCH FOUNDATION', 'LIVING BEYOND BREAST CANCER', 'FIGHT COLORECTAL CANCER',
     'CURE CHILDHOOD CANCER', 'KIDNEY CANCER ASSOCIATION', 'AIDS UNITED', 'ORGANIZATION FOR AUTISM RESEARCH',
     'CAN DO MULTIPLE SCLEROSIS', 'SAN DIEGO CENTER FOR THE BLIND', 'DIABETES FOUNDATION OF MISSISSIPPI',
     'THE ASSOCIATION FOR FRONTOTEMPORAL DEGENERATION', 'FISHER CENTER FOR ALZHEIMER`S RESEARCH FOUNDATION',
     'THE JED FOUNDATION', 'THE TREVOR PROJECT', 'TRAGEDY ASSISTANCE PROGRAM FOR SURVIVORS', 'THE GLOBAL ORPHAN PROJECT',
     'HELP THE HELPLESS', 'PREVENT CHILD ABUSE AMERICA', 'SAVE THE CHILDREN', 'CHRISTIAN RELIEF FUND', 'ALL HANDS AND HEARTS',
     'SBP', 'SAMARITAN`S PURSE', 'UNITED METHODIST COMMITTEE ON RELIEF OF GLOBAL MINISTRIES', 'INTERNATIONAL RELIEF TEAMS',
     'SEMPER FI & AMERICA`S FUND', 'FISHER HOUSE FOUNDATION', 'SOLDIERS` ANGELS', 'OUR MILITARY KIDS', 'BUILDING HOMES FOR HEROES',
     'MEMORIAL ASSISTANCE MINISTRIES', 'TRANSITIONS', 'ROSIE`S PLACE', 'HEALTHCARE FOR THE HOMELESS - HOUSTON',
     'CHICAGO COALITION FOR THE HOMELESS', 'ALIGHT', 'REFUGEES INTERNATIONAL', 'PREEMPTIVE LOVE', 'THE TIBET FUND',
     'UNITED PALESTINIAN APPEAL', 'WOMEN IN DISTRESS OF BROWARD COUNTY', 'ALTERNATIVES', 'THE FAMILY PLACE', 'SAFEHOUSE DENVER',
     'LYDIA`S HOUSE', 'AMERICANS FOR IMMIGRANT JUSTICE', 'JUSTICE IN AGING', 'CAMPHILL VILLAGE KIMBERTON HILLS',
     'STATE VOICES', 'RAINIER SCHOLARS', 'ANIMAL DEFENSE LEAGUE OF TEXAS', 'THE DIAN FOSSEY GORILLA FUND INTERNATIONAL',
     'MICHIGAN ANTI-CRUELTY SOCIETY', 'CHEETAH CONSERVATION FUND', 'RE- WILD']


    # charities = ['ACTION AGAINST HUNGER', 'FEED MY STARVING CHILDREN', 'FACING HUNGER FOODBANK', 'THE HUNGER COALITION']

    # anonymity = public or anonymous
    anonymity = ["PUBLIC"] * int(num_charities/2) + ["ANONYMOUS"] * int(num_charities/2)

    #Compensation per 1/2 hour of participation
    # compensation = c(5)

    max_tasks = 20
    slider_value = 1
    match = ['YES', 'NO']

    #questionnaires
    WEW_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
                "item item-7", "item item-8", "item item-9", "item item-10", "item item-11", "item item-12",
                "item item-13", "item item-14"]
    CEAS_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
                "item item-7", "item item-8"]
    CEAS2_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5"]
    SubC_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
                "item item-7", "item item-8", "item item-9", "item item-10"]
    SAQ_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
               "item item-7", "item item-8", "item item-9", "item item-10"]
    NPI_num = ["item item-1", "item item-2", "item item-3", "item item-4", "item item-5", "item item-6",
               "item item-7", "item item-8", "item item-9"]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            # randomize
            for player in self.get_players():
                player.participant.vars['orderWEW1'] = random.sample(Constants.WEW_num, 14)
                # player.participant.vars['orderWEW2'] = random.sample(Constants.WEW_num, 14)
                player.participant.vars['orderWEW3'] = random.sample(Constants.WEW_num, 14)
                player.participant.vars['orderCEAS1'] = random.sample(Constants.CEAS_num, 8)
                player.participant.vars['orderCEAS2'] = random.sample(Constants.CEAS2_num, 5)
                player.participant.vars['orderSubC'] = random.sample(Constants.SubC_num, 10)
                player.participant.vars['orderSAQ'] = random.sample(Constants.SAQ_num, 10)
                player.participant.vars['orderNPI'] = random.sample(Constants.NPI_num, 9)
                player.participant.vars['orderTask1'] = random.sample(Constants.charities, Constants.num_charities)
                player.participant.vars['orderTask2'] = random.sample(Constants.charities, Constants.num_charities)
                #player.participant.vars['dictVersion'] = random.sample(Constants.versions, Constants.num_charities*2)
                player.participant.vars['dictAnonym'] = random.sample(Constants.anonymity, Constants.num_charities)
                # player.participant.vars['payRound'] = random.randint(Constants.num_charities, Constants.num_rounds)
                player.participant.vars['matchedDonation'] = random.sample(Constants.match, 1)
                player.participant.vars['end_experiment'] = False
                player.participant.vars['already_donated'] = 0
                player.participant.vars['tot_pub_don'] = 0
                player.participant.vars['tasks_completed'] = 0
                player.participant.vars['chosen_char'] = list()
                player.participant.vars['consent'] = False
                player.participant.vars['name_consent'] = ''
                player.participant.vars['num_char_donated'] = 0
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

    SIS = models.IntegerField()
    future = models.IntegerField()
    email = models.StringField(blank=True)

    deservingness = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                        widget=widgets.RadioSelectHorizontal(attrs={'class': 'deser'}))
    closeness = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                    widget=widgets.RadioSelectHorizontal(attrs={'class': 'close'}))

    task_decision = models.StringField(choices=['ANONYMOUS', 'PUBLIC', 'NO'])
    tasks_completed = models.IntegerField()
    # max_to_donate = models.IntegerField(min=0, max=Constants.val_endowment)
    donation = models.DecimalField(max_digits=4, decimal_places=2)

    # def donation_max(self):
    #     return self.max_to_donate
    #
    # def donation_min(self):
    #     return self.min_to_donate
    #
    # def set_payoffs(self):
    #     self.payoff = Constants.endowment - self.donation

    #DEM
    gender = models.StringField(choices=['Female', 'Male', 'Non-binary', 'Other', 'Rather not say'],
                                verbose_name='Which gender do you identify with the most?',
                                widget=widgets.RadioSelect,)
    age = models.IntegerField(verbose_name='What is your age? (Leave blank if you rather not say)', min=18, max=75,
                              blank=True)
    ethnicity = models.StringField(choices=['Hispanic or Latino', 'Non Hispanic or Latino', 'Rather not say'],
                                   verbose_name='Which ethnicity would you describe yourself as?',
                                   widget=widgets.RadioSelect)
    race= models.StringField(choices=['American Indian/Alaska Native', 'Asian', 'Black or African American',
                                      'Native Hawaiian or Other Pacific Islander','White', 'Two or More', 'Rather not say'],
                             verbose_name='Which racial category would you describe yourself as?',
                             widget=widgets.RadioSelect)

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


    # CEAS
    CEAS11 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS12 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS13 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS14 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS15 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS16 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS17 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS18 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS21 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS22 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS23 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS24 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)
    CEAS25 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal)


    #SubC
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

    #SAQ
    SAQ1 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ2 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ3 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ4 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ5 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ6 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ7 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ8 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ9 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))
    SAQ10 = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal(attrs={'class': 'saq'}))

    #NPI
    NPI1 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI2 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    # NPI3 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI4 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI5 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    # NPI6 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI7 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI8 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    # NPI9 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI10 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI11 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    # NPI12 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)
    NPI13 = models.IntegerField(choices=[0, 1], widget=widgets.RadioSelect)

    charity_task_1 = models.StringField()
    charity_task_2 = models.StringField()
    anonymity_task_2 = models.StringField()
    total_subject_donation = models.CurrencyField(min=0, max=Constants.max_tasks)
    matched_donation = models.StringField()
    # consent = models.IntegerField()
    # name_consent = models.StringField(blank=True)
    # listed = models.StringField()

    ST1 = models.IntegerField()

    def ST1_error_message(self, value):
        if value != 50:
            return 'Please position slider at 50'

    ST2 = models.IntegerField()

    def ST2_error_message(self, value):
        if value != 50:
            return 'Please position slider at 50'

    ST3 = models.IntegerField(blank=True)
    ST4 = models.IntegerField(blank=True)
    ST5 = models.IntegerField(blank=True)
    ST6 = models.IntegerField(blank=True)
    ST7 = models.IntegerField(blank=True)
    # ST8 = models.IntegerField(blank=True)
    # ST9 = models.IntegerField(blank=True)
    # ST10 = models.IntegerField(blank=True)
    # ST11 = models.IntegerField(blank=True)
    # ST12 = models.IntegerField(blank=True)

    # S1 = models.IntegerField(blank=True)
    # S2 = models.IntegerField(blank=True)
    # S3 = models.IntegerField(blank=True)
    # S4 = models.IntegerField(blank=True)
    # S5 = models.IntegerField(blank=True)
    # S6 = models.IntegerField(blank=True)
    # S7 = models.IntegerField(blank=True)
    # S8 = models.IntegerField(blank=True)
    # S9 = models.IntegerField(blank=True)
    # S10 = models.IntegerField(blank=True)

    CST = models.DecimalField(max_digits=40, decimal_places=2)






# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'round_number', 'OrderTask1', 'deservingness', 'closeness',
#            'OrderTask2', 'anonymity', 'task_decision']
#     for p in players:
#         yield [p.participant.code,  p.round_number, p.charity_task_1, p.deservingness, p.closeness,
#                p.charity_task_2, p.anonymity_task_2, p.task_decision]


# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'round_number', 'ST3', 'ST4', 'ST5', 'ST6', 'ST7','CST', 'tasks_completed']
#     for p in players:
#         yield [p.participant.code, p.round_number, p.ST3, p.ST4, p.ST5, p.ST6, p.ST7, p.CST, p.tasks_completed]


# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'round_number',
#            'age', 'gender', 'race', 'ethnicity',
#            'WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11', 'WEW12',
#            'WEW13', 'WEW14',
#            'CEAS11', 'CEAS12', 'CEAS13', 'CEAS14', 'CEAS15', 'CEAS16', 'CEAS17', 'CEAS18',
#            'CEAS21', 'CEAS22', 'CEAS23', 'CEAS24', 'CEAS25',
#            'SubC1', 'SubC2', 'SubC3', 'SubC4', 'SubC5', 'SubC6', 'SubC7', 'SubC8', 'SubC9', 'SubC10',
#            'SAQ1', 'SAQ2', 'SAQ3', 'SAQ4', 'SAQ5', 'SAQ6', 'SAQ7', 'SAQ8', 'SAQ9', 'SAQ10',
#            'NPI1', 'NPI2', 'NPI4', 'NPI5', 'NPI7', 'NPI8', 'NPI10', 'NPI11', 'NPI13']
#     for p in players:
#         yield [p.participant.code, p.round_number,
#                p.age, p.gender, p.race, p.ethnicity,
#                p.WEW1, p.WEW2, p.WEW3, p.WEW4, p.WEW5, p.WEW6, p.WEW7, p.WEW8, p.WEW9, p.WEW10, p.WEW11, p.WEW12,
#                p.WEW13, p.WEW14,
#                p.CEAS11, p.CEAS12, p.CEAS13, p.CEAS14, p.CEAS15, p.CEAS16, p.CEAS17, p.CEAS18,
#                p.CEAS21, p.CEAS22, p.CEAS23, p.CEAS24, p.CEAS25,
#                p.SubC1, p.SubC2, p.SubC3, p.SubC4, p.SubC5, p.SubC6, p.SubC7, p.SubC8, p.SubC9, p.SubC10,
#                p.SAQ1, p.SAQ2, p.SAQ3, p.SAQ4, p.SAQ5, p.SAQ6, p.SAQ7, p.SAQ8, p.SAQ9, p.SAQ10,
#                p.NPI1, p.NPI2, p.NPI4, p.NPI5, p.NPI7, p.NPI8, p.NPI10, p.NPI11, p.NPI13]


def custom_export(players):
    # Title row
    yield ['round_number', 'future', 'email']
    for p in players:
        yield [p.round_number, p.future, p.email]

# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'part_label','round_number']
#     for p in players:
#         yield [p.participant.code, p.participant.label, p.round_number ]


# def custom_export(players):
#     # Title row
#     yield ['participant_code', 'round_number', 'matched_donation' ]
#     for p in players:
#         yield [p.participant.code, p.round_number, p.matched_donation ]


# def custom_export(players):
#     # Title row
#     yield ['participant_code','round_number',
#     'OrderTask2', 'anonymity', 'donation', 'matched_donation' ]
#     for p in players:
#         yield [p.participant.code, p.round_number,
#         p.charity_task_2, p.anonymity_task_2, p.donation, p.matched_donation]