from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import (
    Currency as c
)
import time
import random


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'num_charities': Constants.num_charities,
            'max_tasks': Constants.max_tasks,
            'part_pool': self.player.participant.vars['part_pool'],
        }


class Instructions2(Page):
    form_model = 'player'
    form_fields = ['STI1', 'STI2']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'max_tasks': Constants.max_tasks,
            'slider_value': Constants.slider_value,
            'part_pool': self.player.participant.vars['part_pool'],
        }


class InstructionsTrial(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['STT1', 'STT2', 'STT3', 'STT4', 'STT5']

    def is_displayed(self):
        return self.subsession.round_number == 1

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
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {

        }


class Instructionsf(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):

        return {
            'slider_value': Constants.slider_value,
            'max_tasks': Constants.max_tasks,
            'num_charities': Constants.num_charities,
            'part_pool': self.player.participant.vars['part_pool'],

        }


class DT(Page):
    form_model = 'player'
    form_fields = ['tasks_committed']

    def vars_for_template(self):
        self.player.charity = self.player.participant.vars['orderDT'][(self.subsession.round_number - 1)]

        return {
            'charity': self.player.charity,
            'image_path_info': 'dt/pics/{} short.jpg'.format(self.player.charity),
            'round_num': self.subsession.round_number,
            'num_rounds': Constants.num_rounds,
            'max_tasks': Constants.max_tasks,
            'part_pool': self.player.participant.vars['part_pool'],

        }


class ThankYou(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.chosen_charity = self.player.in_round(self.player.participant.vars['this_round']).charity
        self.player.chosen_tasks_committed = self.player.in_round(self.player.participant.vars['this_round']).tasks_committed

        if self.player.chosen_tasks_committed > 0:
            cont = 'YES'
        else:
            cont = 'NO'

        self.player.participant.vars['chosen_charity'] = self.player.chosen_charity
        self.player.participant.vars['chosen_tasks_committed'] = self.player.chosen_tasks_committed

        return {
            'cont': cont,
            'chosen_charity': self.player.chosen_charity,
            'chosen_tasks_committed': self.player.chosen_tasks_committed,
            'slider_value': Constants.slider_value,
            'part_pool': self.player.participant.vars['part_pool'],
        }


page_sequence = [
    Introduction,
    Instructions2,
    InstructionsTrial,
    CAEST,
    Instructionsf,
    DT,
    ThankYou,

]
