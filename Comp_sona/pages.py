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
    form_fields = ['NPI1', 'NPI2', 'NPI4', 'NPI5', 'NPI7', 'NPI8', 'NPI10', 'NPI11', 'NPI13']

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
    form_fields = ['task_decision']

    def is_displayed(self):
        return self.subsession.round_number >= Constants.num_charities and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        round_num = self.subsession.round_number - Constants.num_charities + 1
        self.player.charity_task_2 = self.player.participant.vars['orderTask2'][(round_num-1)]

        for_norder = ["item item-3", "item item-5"]
        norder = random.choice(for_norder)
        if norder == "item item-3":
            for_yorder = ["item item-4", "item item-5"]
            yorder = random.sample(for_yorder, 2)
        else:
            for_yorder = ["item item-3", "item item-4"]
            yorder = random.sample(for_yorder, 2)

        return {
            'norder': norder,
            'yorder': yorder,
            'num_rounds': Constants.num_rounds,
            'max_tasks': Constants.max_tasks,
            'tasks_completed': self.player.participant.vars['tasks_completed'],
            'tasks_allowed': Constants.max_tasks - self.player.participant.vars['tasks_completed'],
            'round_num': round_num,
            'last_charity': Constants.num_charities,
            'charity': self.player.charity_task_2,
            'image_path_info': 'Comp_sona/pics/{} short.jpg'.format(self.player.charity_task_2),
        }

    def before_next_page(self):
        self.player.anonymity_task_2 = self.player.task_decision
        if self.player.participant.vars['tasks_completed'] == 20:
            self.player.task_decision = 'NO'
        if self.player.participant.vars['tasks_completed'] < 20:
            if self.player.task_decision == 'ANONYMOUS':
                self.player.participant.vars['tasks_completed'] += 1
                self.player.participant.vars['chosen_char'].append((self.player.charity_task_2, self.player.anonymity_task_2))
            elif self.player.task_decision == "PUBLIC":
                self.player.participant.vars['tasks_completed'] += 1
                self.player.participant.vars['chosen_char'].append((self.player.charity_task_2, self.player.anonymity_task_2))
            else:
                pass



# class SliderTask(Page):
#     timeout_seconds = 60
#     form_model = 'player'
#     form_fields = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
#
#     def is_displayed(self):
#         return self.subsession.round_number >= Constants.num_charities and self.participant.vars[
#             'end_experiment'] is False and self.player.in_round(self.subsession.round_number).task_decision is True
#
#     def vars_for_template(self):
#         round_num = self.subsession.round_number - Constants.num_charities + 1
#         for_marg = range(0, 210+1, 10)
#         marg = random.choices(for_marg, weights=None, cum_weights=None, k=10)
#
#         return {
#             'num_rounds': Constants.num_rounds,
#             'round_num': round_num,
#             'last_charity': Constants.num_charities,
#             'marg': marg
#         }
#
#     def before_next_page(self):
#         don = 0
#         slider_position = [self.player.S1, self.player.S2, self.player.S3, self.player.S4, self.player.S5,
#                            self.player.S6, self.player.S7, self.player.S8, self.player.S9, self.player.S10]
#         for i in slider_position:
#             if i == 50:
#                 don += Constants.slider_value
#             else:
#                 pass
#         self.player.donation = don
#         if self.player.anonymity_task_2 == "PUBLIC":
#             self.player.participant.vars['tot_pub_don'] += self.player.donation
#         else:
#             pass


class ThankYou(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_experiment'] == False

    def vars_for_template(self):
        time_spent = (self.player.participant.vars['time_end'] - self.player.participant.vars['time_start'])/60

        if len(self.player.participant.vars['chosen_char']) > 0:
            cont = 'YES'
        else:
            cont = 'NO'

        random.shuffle(self.player.participant.vars['chosen_char'])

        # if self.player.participant.vars['tot_pub_don'] >= Constants.max_tasks / 4:
        #     self.player.listed = 'YES'
        # else:
        #     self.player.listed = 'NO'

        self.player.matched_donation = self.player.participant.vars['matchedDonation'][0]

        # self.player.total_subject_donation = sum(self.player.in_all_rounds().donation)
        # self.player.total_subject_donation = self.player.donation
        self.player.participant.vars['matchedDonation'] = self.player.matched_donation
        self.player.tasks_completed = self.player.participant.vars['tasks_completed']

        return {
            'matched_donation': self.player.matched_donation,
            # 'listed': self.player.listed,
            'time_spent': round(time_spent),
            'tasks_completed': self.player.participant.vars['tasks_completed'],
            'cont': cont,
            'check': self.player.participant.vars['chosen_char'],
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
    Dem,
    WEW1,
    InstructionsFT,
    FirstTask,
    InstructionsST,
    InstructionsST1,
    InstructionsST2,
    InstructionsSTtrial,
    CAEST,
    InstructionsSTf,
    SecondTask,
    WEW3,
    CEAS1,
    CEAS2,
    SubC,
    SAQ,
    DYADS,
    ThankYou,
    TY2,
]
