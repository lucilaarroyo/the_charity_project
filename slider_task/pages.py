from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class ShortTask(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['S1', 'S2', 'S3', 'S4', 'S5']

    def is_displayed(self):
        return self.subsession.round_number <= len(self.player.participant.vars['chosen_char']) and \
               self.participant.vars['end_experiment'] is False

    def vars_for_template(self):
        round_num = self.subsession.round_number
        char_and_anon = self.player.participant.vars['chosen_char'][round_num-1]
        self.player.charity = char_and_anon[0]
        self.player.anonymity = char_and_anon[1]
        self.player.matched_donation = self.player.participant.vars['matchedDonation'][0]

        for_marg = range(0, 570+1, 10)
        marg = random.sample(for_marg, k=5)

        return {
            'num_rounds': len(self.player.participant.vars['chosen_char']),
            'round_num': round_num,
            'marg': marg,
            # 'image_path_info': 'Comp_sona/pics/{} short.jpg'.format(self.player.charity),
            'charity': self.player.charity,
            'anonymity': self.player.anonymity,

        }

    def before_next_page(self):
        num_sliders = 0
        slider_position = [self.player.S1, self.player.S2, self.player.S3, self.player.S4, self.player.S5]
        for i in slider_position:
            if i == 50:
                num_sliders += 1
            else:
                pass
        if num_sliders == 5:
            don = Constants.slider_value
        else:
            don = 0
        self.player.donation = don
        self.player.participant.vars['num_char_donated'] += self.player.donation
        if self.player.anonymity == "PUBLIC":
            self.player.participant.vars['tot_pub_don'] += self.player.donation
        else:
            pass


# class TasksWaitPage(WaitPage):
#     def is_displayed(self):
#         return self.subsession.round_number <= len(self.player.participant.vars['chosen_char']) and \
#                self.participant.vars['end_experiment'] is False


class PostTaskPage(Page):
    def is_displayed(self):
        return self.subsession.round_number <= len(self.player.participant.vars['chosen_char']) and \
               self.participant.vars['end_experiment'] is False

    def vars_for_template(self):
        round_num = self.subsession.round_number
        if round_num == len(self.player.participant.vars['chosen_char']):
            if self.player.participant.vars['tot_pub_don'] >= (Constants.num_rounds / 2):
                self.player.listed = 'YES'
            else:
                self.player.listed = 'NO'

        return {
            'num_rounds': len(self.player.participant.vars['chosen_char']),
            'round_num': round_num,
            'don': self.player.donation,
            'num_char_donated': self.player.participant.vars['num_char_donated'],

        }


page_sequence = [ShortTask, PostTaskPage]
