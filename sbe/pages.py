from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class PreDots(Page):
    timeout_seconds = 3

    def vars_for_template(self):
        round_num = self.subsession.round_number
        if round_num <= (Constants.num_trial_rounds/2):
            self.player.role_in_round = self.player.participant.vars['role_1']
        elif round_num <= Constants.num_trial_rounds:
            self.player.role_in_round = self.player.participant.vars['role_2']
        else:
            self.player.role_in_round = self.player.participant.vars['role_3']

        if round_num <= Constants.num_trial_rounds:
            self.player.num_of_dots = self.player.participant.vars['dots_displayed_trial'][(round_num-1)]
        else:
            self.player.num_of_dots = self.player.participant.vars['dots_displayed'][(round_num-Constants.num_trial_rounds-1)]

        if self.player.role_in_round == 'Advisor':
            for_margins_left = range(30, 1240+1, 15)
            for_margins_top = range(20, 720+1, 15)
            margins_left = random.sample(for_margins_left, self.player.num_of_dots)
            margins_top = random.sample(for_margins_top, self.player.num_of_dots)
            self.player.participant.vars['m_l'] = margins_left
            self.player.participant.vars['m_t'] = margins_top


        return {
            'role': self.player.role_in_round,
            # 'm_l': margins_left,
            # 'm_t': margins_top,
            'num_dots': self.player.num_of_dots,


        }




class DotsAdv(Page):
    timeout_seconds = 3

    def is_displayed(self):
        return self.player.role_in_round == 'Advisor'

    def vars_for_template(self):



        return {
            'role': self.player.role_in_round,
            'm_l': self.player.participant.vars['m_l'],
            'm_t': self.player.participant.vars['m_t'],
            'num_dots': self.player.num_of_dots,


        }


class Adv(Page):
    form_model = 'player'
    form_fields = ['advice']
    timeout_seconds = 60

    def is_displayed(self):
        return self.player.role_in_round == 'Advisor'

    def vars_for_template(self):



        return {
            'role': self.player.role_in_round,

            'num_dots': self.player.num_of_dots,


        }


class AdvWaitPage(WaitPage):
    def vars_for_template(self):




        return {


        }



class DotsDec(Page):
    timeout_seconds = 3

    def is_displayed(self):
        return self.player.role_in_round == 'Decider'

    def vars_for_template(self):

        for pl in self.player.get_others_in_group():
            self.player.participant.vars['m_l'] = pl.participant.vars['m_l']
            self.player.participant.vars['m_t'] = pl.participant.vars['m_t']


        return {
            'role': self.player.role_in_round,
            'm_l': self.player.participant.vars['m_l'],
            'm_t': self.player.participant.vars['m_t'],
            'num_dots': self.player.num_of_dots,


        }


class Dec(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_seconds = 60

    def is_displayed(self):
        return self.player.role_in_round == 'Decider'

    def vars_for_template(self):
        for pl in self.player.get_others_in_group():
            advice = pl.advice


        return {
            'advice': advice


        }


class DecWaitPage(WaitPage):
    def vars_for_template(self):




        return {
            'decision': self.player.decision,
            'advice_given': self.player.advice,

        }

# class ResultsWaitPage(WaitPage):
#     pass


# class Results(Page):
#     pass


page_sequence = [
    PreDots,
    DotsAdv,
    Adv,
    AdvWaitPage,
    DotsDec,
    Dec,
    DecWaitPage,

]
