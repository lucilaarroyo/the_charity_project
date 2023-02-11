from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Instructions(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        self.player.rolee = self.player.participant.vars['role']
        self.player.difficulty = self.player.participant.vars['difficulty']

        return {
            'num_actual_rounds': Constants.num_actual_rounds,
            'num_trial_rounds': Constants.num_trial_rounds,
            'role': self.player.rolee,
            'round_multiplier': Constants.round_multiplier,
            'dots_secs': Constants.dots_secs,

        }


class WP(WaitPage):
    template_name = 'sbe/WP.html'

    def vars_for_template(self):
        round_num = self.subsession.round_number
        for_margins_left = range(30, 1240 + 1, 15)
        for_margins_top = range(20, 720 + 1, 15)
        if round_num <= Constants.num_trial_rounds:
            # self.player.num_of_dots = self.player.participant.vars['dots_displayed_trial'][(round_num - 1)]
            for g in self.subsession.get_groups():
                num_dots = g.get_player_by_id(1).participant.vars['dots_displayed_trial'][(round_num - 1)]
                margins_left = random.sample(for_margins_left, num_dots)
                margins_top = random.sample(for_margins_top, num_dots)
                for p in g.get_players():
                    p.participant.vars['m_l'] = margins_left
                    p.participant.vars['m_t'] = margins_top

        else:
            # self.player.num_of_dots = self.player.participant.vars['dots_displayed'][(round_num - Constants.num_trial_rounds - 1)]
            for g in self.subsession.get_groups():
                num_dots = g.get_player_by_id(1).participant.vars['dots_displayed'][
                    (round_num - Constants.num_trial_rounds - 1)]
                margins_left = random.sample(for_margins_left, num_dots)
                margins_top = random.sample(for_margins_top, num_dots)
                for p in g.get_players():
                    p.participant.vars['m_l'] = margins_left
                    p.participant.vars['m_t'] = margins_top

        return {
            'round_num': round_num,


        }


class PreDots(Page):
    timeout_seconds = 15

    def vars_for_template(self):
        round_num = self.subsession.round_number
        if round_num <= Constants.num_trial_rounds:
            self.player.num_of_dots = self.player.participant.vars['dots_displayed_trial'][(round_num - 1)]
        else:
            self.player.num_of_dots = self.player.participant.vars['dots_displayed'][(round_num - Constants.num_trial_rounds - 1)]

        return {
            'role': self.player.participant.vars['role'],
            'num_dots': self.player.num_of_dots,
            'round_num': round_num,
            'round_count': round_num - Constants.num_trial_rounds,
            'm_l': self.player.participant.vars['m_l'],
            'm_t': self.player.participant.vars['m_t']

        }


class DotsAdv(Page):
    timeout_seconds = Constants.sec_adv_sees

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

    def is_displayed(self):
        return self.player.role_in_round == 'Advisor'

    def vars_for_template(self):



        return {
            'role': self.player.role_in_round,

            'num_dots': self.player.num_of_dots,


        }

    def before_next_page(self):
        if self.player.num_of_dots < 20 and self.player.advice == 'LESS':
            self.player.correct_advice = 1
        elif self.player.num_of_dots > 20 and self.player.advice == 'MORE':
            self.player.correct_advice = 1
        else:
            self.player.correct_advice = 0


class AdvWaitPage(WaitPage):
    def vars_for_template(self):



        return {



        }



class DotsDec(Page):
    timeout_seconds = Constants.sec_dec_sees

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

    def is_displayed(self):
        return self.player.role_in_round == 'Decider'

    def vars_for_template(self):
        for pl in self.player.get_others_in_group():
            advice = pl.advice


        return {
            'advice': advice


        }

    def before_next_page(self):
        if self.player.num_of_dots < 20 and self.player.decision == 'LESS':
            self.player.correct_decision = 1
        elif self.player.num_of_dots > 20 and self.player.decision == 'MORE':
            self.player.correct_decision = 1
        else:
            self.player.correct_decision = 0


class DecWaitPage(WaitPage):
    def vars_for_template(self):




        return {
            'decision': self.player.decision,
            'advice_given': self.player.advice,

        }


class RoundResult(Page):
    def vars_for_template(self):
        round_num = self.subsession.round_number

        if self.player.role_in_round == 'Advisor':
            advice = self.player.advice
            correct_advice = self.player.correct_advice
            for pl in self.player.get_others_in_group():
                decision = pl.decision
                correct_decision = pl.correct_decision
        else:
            decision = self.player.decision
            correct_decision = self.player.correct_decision
            for pl in self.player.get_others_in_group():
                advice = pl.advice
                correct_advice = pl.correct_advice

        return {
            'advice': advice,
            'correct_advice': correct_advice,
            'decision': decision,
            'correct_decision': correct_decision,
            'round_num': round_num,
            'round_count': round_num - Constants.num_trial_rounds,

        }


class BeforeNextRound(WaitPage):
    def vars_for_template(self):




        return {


        }


# class Results(Page):

page_sequence = [
    Instructions,
    WP,
    PreDots,
    # DotsAdv,
    # Adv,
    # AdvWaitPage,
    # DotsDec,
    # Dec,
    # DecWaitPage,
    # RoundResult,
    # BeforeNextRound,


]
