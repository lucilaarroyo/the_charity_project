from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Instructions(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        self.player.difficulty = self.player.participant.vars['difficulty']
        self.player.num_extra_rounds = self.player.participant.vars['num_extra_rounds']
        if self.player.difficulty == 'Easy':
            num_easy_rounds = (2/3) * self.player.num_extra_rounds
            num_hard_rounds = (1/3) * self.player.num_extra_rounds
            extra_dots_displayed = random.choices(Constants.num_dots_easy, k=num_easy_rounds) + random.choices(Constants.num_dots_hard, k=num_hard_rounds)
            random.shuffle(extra_dots_displayed)
            self.player.participant.vars['extra_dots_displayed'] = extra_dots_displayed
        else:
            num_easy_rounds = (1 / 3) * self.player.num_extra_rounds
            num_hard_rounds = (2 / 3) * self.player.num_extra_rounds
            extra_dots_displayed = random.choices(Constants.num_dots_easy, k=num_easy_rounds) + random.choices(
                Constants.num_dots_hard, k=num_hard_rounds)
            random.shuffle(extra_dots_displayed)
            self.player.participant.vars['extra_dots_displayed'] = extra_dots_displayed

        return {
            'num_extra_rounds': self.player.num_extra_rounds,
            'extra_dots_displayed': self.player.participant.vars['extra_dots_displayed'],
            'dots_secs': Constants.dots_secs,

        }


class PreDots(Page):
    timeout_seconds = 3
    timer_text = 'Dots will be displayed in: '

    def is_displayed(self):
        return self.subsession.round_number <= self.player.participant.vars['num_extra_rounds']

    def vars_for_template(self):
        round_num = self.subsession.round_number
        self.player.num_of_dots = self.player.participant.vars['extra_dots_displayed'][(round_num - 1)]

        for_margins_left = range(30, 1240 + 1, 15)
        for_margins_top = range(20, 720 + 1, 15)
        self.player.participant.vars['m_l'] = random.sample(for_margins_left, self.player.num_dots)
        self.player.participant.vars['m_t'] = random.sample(for_margins_top, self.player.num_dots)

        return {
            'num_dots': self.player.num_of_dots,
            'round_num': round_num,
            'm_l': self.player.participant.vars['m_l'],
            'm_t': self.player.participant.vars['m_t'],

        }


class Dots(Page):
    timeout_seconds = Constants.dots_secs

    def is_displayed(self):
        return self.subsession.round_number <= self.player.participant.vars['num_extra_rounds']

    def vars_for_template(self):

        return {
            'm_l': self.player.participant.vars['m_l'],
            'm_t': self.player.participant.vars['m_t'],
            'num_dots': self.player.num_of_dots,

        }


class Dec(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return self.subsession.round_number <= self.player.participant.vars['num_extra_rounds']

    def vars_for_template(self):

        return {


        }

    def before_next_page(self):
        if self.player.num_of_dots < 20 and self.player.decision == 'LESS':
            self.player.correct_decision = 1
        elif self.player.num_of_dots > 20 and self.player.decision == 'MORE':
            self.player.correct_decision = 1
        else:
            self.player.correct_decision = 0


class RoundResult(Page):
    def is_displayed(self):
        return self.subsession.round_number <= self.player.participant.vars['num_extra_rounds']

    def vars_for_template(self):
        round_num = self.subsession.round_number

        if self.player.correct_decision == 0:
            result = "INCORRECT"
        else:
            result = "CORRECT"

        return {
            'round_num': round_num,
            'result': result,
            'num_extra_rounds': self.player.participant.vars['num_extra_rounds'],
        }


class TaskResult(Page):
    def is_displayed(self):
        return self.subsession.round_number == self.player.participant.vars['num_extra_rounds']

    def vars_for_template(self):
        num_adv_rounds = Constants.num_actual_rounds/2
        self.player.num_adv_incorrect = num_adv_rounds - self.player.participant.vars['num_correct_adv']

        for p in self.player.get_others_in_group():
            if self.player.participant.vars['num_correct_adv'] != p.participant.vars['num_correct_adv']:
                check = "ERROR"
            else:
                check = "GOOD JOB"

        self.player.num_extra_rounds = self.player.num_adv_incorrect * Constants.round_multiplier

        if self.player.participant.vars['role'] == 'Decider':
            self.player.participant.vars['num_extra_rounds'] = self.player.num_extra_rounds

        return {
            'num_actual_rounds': Constants.num_actual_rounds,
            'num_adv_incorrect': self.player.num_adv_incorrect,
            'round_multiplier': Constants.round_multiplier,
            'num_extra_rounds': self.player.num_extra_rounds,
            'check': check,

        }

    def app_after_this_page(self, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if self.player.participant.vars['role'] == 'Advisor':
            return "dt"


page_sequence = [
    # Instructions,
    PreDots,
    Dots,
    Dec,
    RoundResult,
    TaskResult,

]
