from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import (
    Currency as c
)
import time
import random


class SIS(Page):
    form_model = 'player'
    form_fields = ['future','email', 'SIS']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        self.player.participant.vars['time_start'] = time.time()
        return {

        }

    def before_next_page(self):
        if self.player.SIS == 0:
            self.player.participant.vars['end_experiment'] = True
        else:
            pass


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1 and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            # 'compensation': Constants.compensation,
        }


class Dem(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'ethnicity', 'race']

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {

        }


class WEW1(Page):
    form_model = 'player'
    form_fields = ['WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11',
                   'WEW12', 'WEW13', 'WEW14']

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'WEW1_num': self.player.participant.vars['orderWEW1'],
        }


# class WEW2(Page):
#     form_model = 'player'
#     form_fields = ['WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11',
#                    'WEW12', 'WEW13', 'WEW14']
#
#     def is_displayed(self):
#         return self.subsession.round_number == Constants.num_charities and self.participant.vars['end_experiment'] == False
#
#     def vars_for_template(self):
#         return {
#             'WEW1_num': self.player.participant.vars['orderWEW2'],
#         }


class WEW3(Page):
    form_model = 'player'
    form_fields = ['WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11',
                   'WEW12', 'WEW13', 'WEW14']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'WEW1_num': self.player.participant.vars['orderWEW3'],
        }


class CEAS1(Page):
    form_model = 'player'
    form_fields = ['CEAS11', 'CEAS12', 'CEAS13', 'CEAS14', 'CEAS15', 'CEAS16', 'CEAS17', 'CEAS18']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'CEAS_num': self.player.participant.vars['orderCEAS1'],
        }


class CEAS2(Page):
    form_model = 'player'
    form_fields = ['CEAS21', 'CEAS22', 'CEAS23', 'CEAS24', 'CEAS25']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'CEAS2_num': self.player.participant.vars['orderCEAS2'],
        }


class SubC(Page):
    form_model = 'player'
    form_fields = ['SubC1', 'SubC2', 'SubC3', 'SubC4', 'SubC5', 'SubC6', 'SubC7', 'SubC8', 'SubC9', 'SubC10']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'SubC_num': self.player.participant.vars['orderSubC'],
        }


class SAQ(Page):
    form_model = 'player'
    form_fields = ['SAQ1', 'SAQ2', 'SAQ3', 'SAQ4', 'SAQ5', 'SAQ6', 'SAQ7', 'SAQ8', 'SAQ9', 'SAQ10']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'SAQ_num': self.player.participant.vars['orderSAQ'],
        }


class DYADS(Page):
    form_model = 'player'
    form_fields = ['NPI1', 'NPI2', 'NPI3', 'NPI4', 'NPI5', 'NPI6', 'NPI7', 'NPI8', 'NPI9', 'NPI10', 'NPI11', 'NPI12', 'NPI13']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'NPI_num': self.player.participant.vars['orderNPI'],
        }

    def before_next_page(self):
        self.player.participant.vars['time_end'] = time.time()


class InstructionsFT(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1 and self.participant.vars['end_experiment'] == False


class FirstTask(Page):
    form_model = 'player'
    form_fields = ['deservingness', 'closeness']

    def is_displayed(self):
        return self.subsession.round_number <= Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        charity_num = self.subsession.round_number
        self.player.charity_task_1 = self.player.participant.vars['orderTask1'][(charity_num-1)]

        return {
            'charity_num': charity_num,
            'last_charity': Constants.num_charities,
            'charity': self.player.charity_task_1,
            'image_path_info': 'Comp_sona/pics/{} short.jpg'.format(self.player.charity_task_1),
        }


class InstructionsST(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'max_tasks': Constants.max_tasks,
        }


class InstructionsST1(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'max_tasks': Constants.max_tasks,
        }


class InstructionsST2(Page):
    form_model = 'player'
    form_fields = ['ST1', 'ST2']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'max_tasks': Constants.max_tasks,
            'slider_value': Constants.slider_value,
        }


class InstructionsSTtrial(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['ST3', 'ST4', 'ST5', 'ST6', 'ST7']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        for_marg = range(0, 570+1, 10)
        marg = random.sample(for_marg, k=5)

        return {
            'marg': marg
        }


class CAEST(Page):
    form_model = 'player'
    form_fields = ['CST']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {

        }


class InstructionsSTf(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        return {
            'slider_value': Constants.slider_value,
            'max_tasks': Constants.max_tasks,
        }


class SecondTask(Page):
    form_model = 'player'
    form_fields = ['tasks_committed', 'anonymity_task_2']

    def is_displayed(self):
        return self.subsession.round_number >= Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        round_num = self.subsession.round_number - Constants.num_charities + 1
        self.player.charity_task_2 = self.player.participant.vars['orderTask2'][(round_num-1)]

        for_norder = ["item item-4", "item item-6"]
        norder = random.choice(for_norder)
        if norder == "item item-4":
            for_yorder = ["item item-5", "item item-6"]
            yorder = random.sample(for_yorder, 2)
        else:
            for_yorder = ["item item-4", "item item-5"]
            yorder = random.sample(for_yorder, 2)

        return {
            'norder': norder,
            'yorder': yorder,
            'num_rounds': Constants.num_rounds,
            'max_tasks': Constants.max_tasks,
            'round_num': round_num,
            'last_charity': Constants.num_charities,
            'charity': self.player.charity_task_2,
            'image_path_info': 'Comp_sona/pics/{} short.jpg'.format(self.player.charity_task_2),
        }

    # def before_next_page(self):


class ThankYou(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        time_spent = (self.player.participant.vars['time_end'] - self.player.participant.vars['time_start'])/60

        chosen_round = self.player.participant.vars['chosen_round']
        self.player.chosen_charity = self.player.in_round(chosen_round).charity_task_2
        self.player.chosen_anonymity = self.player.in_round(chosen_round).anonymity_task_2
        self.player.chosen_tasks_committed = self.player.in_round(chosen_round).tasks_committed

        if self.player.chosen_tasks_committed > 0 and self.player.chosen_anonymity != "N/A":
            cont = 'YES'
        else:
            cont = 'NO'

        if self.player.chosen_anonymity == "Public":
            self.player.matched_donation = "NO"
        elif self.player.chosen_anonymity == "N/A":
            self.player.matched_donation = "NO"
        else:
            self.player.matched_donation = self.player.participant.vars['matchedDonation'][0]

        self.player.participant.vars['matchedDonation'] = self.player.matched_donation
        self.player.participant.vars['chosen_charity'] = self.player.chosen_charity
        self.player.participant.vars['chosen_anonymity'] = self.player.chosen_anonymity
        self.player.participant.vars['chosen_tasks_committed'] = self.player.chosen_tasks_committed

        return {
            'matched_donation': self.player.matched_donation,
            'time_spent': round(time_spent),
            'cont': cont,
            'chosen_charity': self.player.chosen_charity,
            'chosen_anonymity': self.player.chosen_anonymity,
            'chosen_tasks_committed': self.player.chosen_tasks_committed,
            'slider_value': Constants.slider_value,
        }


class TY2(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.participant.vars['end_experiment'] == True

    def vars_for_template(self):
        return {

        }


page_sequence = [
    SIS,
    Introduction,
    # Dem,
    # WEW1,
    InstructionsFT,
    FirstTask,
    InstructionsST,
    InstructionsST1,
    InstructionsST2,
    InstructionsSTtrial,
    CAEST,
    InstructionsSTf,
    SecondTask,
    # WEW3,
    # CEAS1,
    # CEAS2,
    # SubC,
    # SAQ,
    DYADS,
    ThankYou,
    TY2,
]
