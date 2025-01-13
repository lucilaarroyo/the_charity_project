from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class GWP(WaitPage):
    template_name = 'sbe/GWP.html'
    group_by_arrival_time = True

    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.group.get_player_by_id(1).participant.vars['role'] = random.choice(Constants.roles)
        if self.group.get_player_by_id(1).participant.vars['role'] == Constants.roles[0]:
            self.group.get_player_by_id(2).participant.vars['role'] = Constants.roles[1]
        else:
            self.group.get_player_by_id(2).participant.vars['role'] = Constants.roles[0]

        # need to change if num_trial_rounds changes
        dots_displayed_trial = [random.choice(Constants.num_dots_easy)] + random.choices(Constants.num_dots_hard, k=2)
        random.shuffle(dots_displayed_trial)
        for player in self.group.get_players():
            player.participant.vars['dots_displayed_trial'] = dots_displayed_trial

        #difficulty = random.choice(Constants.level)
        difficulty = 'Hard'
        w_wo_advice = ["Without", "With"] + random.sample(Constants.adv_rounds, (Constants.num_actual_rounds - 2))
        for player in self.group.get_players():
            player.participant.vars['difficulty'] = difficulty
            player.participant.vars['adv_rounds'] = w_wo_advice

        if difficulty == 'Easy':
            dots_displayed_adv = random.choices(Constants.num_dots_easy, k=12) + random.choices(Constants.num_dots_hard, k=3)
            random.shuffle(dots_displayed_adv)
            dots_displayed_dec = random.choices(Constants.num_dots_easy, k=12) + random.choices(Constants.num_dots_hard, k=3)
            random.shuffle(dots_displayed_dec)
            for_dots_displayed = []
            for i in w_wo_advice:
                if i == 'With':
                    for_dots_displayed.append(dots_displayed_adv[0])
                    del dots_displayed_adv[0]
                else:
                    for_dots_displayed.append(dots_displayed_dec[0])
                    del dots_displayed_dec[0]
            for player in self.group.get_players():
                player.participant.vars['dots_displayed'] = for_dots_displayed

        else:
            dots_displayed_adv = random.choices(Constants.num_dots_easy, k=3) + random.choices(Constants.num_dots_hard, k=12)
            random.shuffle(dots_displayed_adv)
            dots_displayed_dec = random.choices(Constants.num_dots_easy, k=3) + random.choices(Constants.num_dots_hard, k=12)
            random.shuffle(dots_displayed_dec)
            for_dots_displayed = []
            for i in w_wo_advice:
                if i == 'With':
                    for_dots_displayed.append(dots_displayed_adv[0])
                    del dots_displayed_adv[0]
                else:
                    for_dots_displayed.append(dots_displayed_dec[0])
                    del dots_displayed_dec[0]
            for player in self.group.get_players():
                player.participant.vars['dots_displayed'] = for_dots_displayed


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

        return {
            'round_num': round_num,
        }

    def after_all_players_arrive(self):
        round_num = self.subsession.round_number
        for_margins_left = range(20, 1000 + 1, 12)
        for_margins_top = range(20, 680 + 1, 12)
        if round_num <= Constants.num_trial_rounds:
            num_dots = self.group.get_player_by_id(1).participant.vars['dots_displayed_trial'][(round_num - 1)]
            margins_left = random.sample(for_margins_left, num_dots)
            margins_top = random.sample(for_margins_top, num_dots)
            for p in self.group.get_players():
                p.participant.vars['m_l'] = margins_left
                p.participant.vars['m_t'] = margins_top
        else:
            num_dots = self.group.get_player_by_id(1).participant.vars['dots_displayed'][(round_num - Constants.num_trial_rounds - 1)]
            margins_left = random.sample(for_margins_left, num_dots)
            margins_top = random.sample(for_margins_top, num_dots)
            for p in self.group.get_players():
                p.participant.vars['m_l'] = margins_left
                p.participant.vars['m_t'] = margins_top


class PreDots(Page):
    timeout_seconds = 3
    timer_text = 'Dots will be displayed in: '

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
            'm_t': self.player.participant.vars['m_t'],
            'adv_rounds': self.player.participant.vars['adv_rounds'],
            'adv_rounds_this_round': self.player.participant.vars['adv_rounds'][(round_num - Constants.num_trial_rounds - 1)],

        }


class Dots(Page):
    timeout_seconds = Constants.dots_secs

    # def is_displayed(self):
    #     return self.player.role_in_round == 'Advisor'

    def vars_for_template(self):

        return {
            'role': self.player.participant.vars['role'],
            'm_l': self.player.participant.vars['m_l'],
            'm_t': self.player.participant.vars['m_t'],
            'num_dots': self.player.num_of_dots,


        }


class Adv(Page):
    form_model = 'player'
    form_fields = ['advice']

    def is_displayed(self):
        return self.subsession.round_number > Constants.num_trial_rounds and self.player.participant.vars['adv_rounds'][self.subsession.round_number - Constants.num_trial_rounds - 1] == "With" and self.player.participant.vars['role'] == 'Advisor'

    def vars_for_template(self):

        return {
            'role': self.player.participant.vars['role'],
            'num_dots': self.player.num_of_dots,
        }

    def before_next_page(self):
        if self.player.participant.vars['role'] == 'Advisor':
            if self.player.num_of_dots == self.player.advice:
                self.player.correct_advice = 1
            else:
                self.player.correct_advice = 0
        self.player.participant.vars['num_correct_adv'] = self.player.participant.vars['num_correct_adv'] + self.player.correct_advice


class AWP(WaitPage):
    template_name = 'sbe/AWP.html'

    def is_displayed(self):
        return self.subsession.round_number > Constants.num_trial_rounds and self.player.participant.vars['adv_rounds'][self.subsession.round_number - Constants.num_trial_rounds - 1] == "With"

    def vars_for_template(self):

        return {


        }


class AdvDec(Page):

    def is_displayed(self):
        return self.subsession.round_number > Constants.num_trial_rounds and self.player.participant.vars['adv_rounds'][self.subsession.round_number - Constants.num_trial_rounds - 1] == "With" and self.player.participant.vars['role'] == 'Advisor'

    def vars_for_template(self):

        return {
            'role': self.player.participant.vars['role'],
            'num_dots': self.player.num_of_dots,
            'advice': self.player.advice,
            'num_cor_adv': self.player.participant.vars['num_correct_adv'],
        }


class Dec(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return self.subsession.round_number <= Constants.num_trial_rounds or self.player.participant.vars['role'] == 'Decider'

    def vars_for_template(self):
        if self.subsession.round_number <= Constants.num_trial_rounds:
            adv_round = "TRIAL"
        else:
            if self.player.participant.vars['adv_rounds'][self.subsession.round_number - Constants.num_trial_rounds - 1] == "With":
                adv_round = "With"
                for p in self.player.get_others_in_group():
                    self.player.decision = p.in_round(self.subsession.round_number).advice
            else:
                adv_round = "Without"


        return {
            'role': self.player.participant.vars['role'],
            'decision': self.player.decision,
            'adv_round': adv_round,


        }

    def js_vars(self):
        return dict(
            decision_adv=self.player.decision,
        )

    def before_next_page(self):
        if self.player.num_of_dots == self.player.decision:
            self.player.correct_decision = 1
        else:
            self.player.correct_decision = 0


class RoundResult(Page):
    # def is_displayed(self):
    #     return self.subsession.round_number <= Constants.num_trial_rounds or self.player.participant.vars['role'] == 'Decider' or self.player.participant.vars['adv_rounds'][self.subsession.round_number - Constants.num_trial_rounds - 1] == "With"

    def vars_for_template(self):
        round_num = self.subsession.round_number

        if self.subsession.round_number <= Constants.num_trial_rounds:
            self.player.correctness = self.player.correct_decision
            adv_round = "TRIAL"
        else:
            if self.player.participant.vars['adv_rounds'][self.subsession.round_number - Constants.num_trial_rounds - 1] == "With":
                adv_round = "With"
                if self.player.participant.vars['role'] == 'Decider':
                    for p in self.player.get_others_in_group():
                        self.player.correctness = p.in_round(self.subsession.round_number).correct_advice
                else:
                    self.player.correctness = self.player.correct_advice

            else:
                adv_round = "Without"
                self.player.correctness = self.player.correct_decision

        if self.player.correctness == 0:
            result = "INCORRECT"
        elif self.player.correctness == 1:
            result = "CORRECT"
        else:
            result = ""

        return {
            'role': self.player.participant.vars['role'],
            'correctness': self.player.correctness,
            'round_num': round_num,
            'round_count': round_num - Constants.num_trial_rounds,
            'adv_round': adv_round,
            'result': result,
            'round_mult': Constants.round_multiplier,

        }

    def before_next_page(self):
        if self.subsession.round_number > Constants.num_trial_rounds and self.player.participant.vars['adv_rounds'][self.subsession.round_number - Constants.num_trial_rounds - 1] == "With":
            if self.player.participant.vars['role'] == 'Decider':
                self.player.participant.vars['num_correct_adv'] = self.player.participant.vars['num_correct_adv'] + self.player.correctness


class TRWP(WaitPage):
    template_name = 'sbe/TRWP.html'

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds


class TaskResult(Page):
    form_model = 'player'
    form_fields = ['performance']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        num_adv_rounds = Constants.num_actual_rounds/2
        self.player.num_adv_incorrect = int(num_adv_rounds) - self.player.participant.vars['num_correct_adv']

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
            'role': self.player.participant.vars['role'],
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
    GWP,
    Instructions,
    WP,
    PreDots,
    Dots,
    Adv,
    AWP,
    AdvDec,
    Dec,
    RoundResult,
    TRWP,
    TaskResult,

]
