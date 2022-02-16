from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class ShortTask(Page):
    timeout_seconds = 60
    form_model = 'player'
    form_fields = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']

    def is_displayed(self):
        return self.subsession.round_number <= len(self.player.participant.vars['chosen_char']) and \
               self.participant.vars['end_experiment'] is False

    def vars_for_template(self):
        round_num = self.subsession.round_number
        char_and_anon = self.player.participant.vars['chosen_char'][round_num-1]
        self.player.charity = char_and_anon[0]
        self.player.anonymity = char_and_anon[1]

        for_marg = range(0, 220+1, 10)
        marg = random.choices(for_marg, weights=None, cum_weights=None, k=10)

        return {
            'num_rounds': len(self.player.participant.vars['chosen_char']),
            'round_num': round_num,
            'marg': marg,
            # 'image_path_info': 'Comp_sona/pics/{} short.jpg'.format(self.player.charity),
            'charity': self.player.charity,
            'anonymity': self.player.anonymity,

        }

    def before_next_page(self):
        don = 0
        slider_position = [self.player.S1, self.player.S2, self.player.S3, self.player.S4, self.player.S5,
                           self.player.S6, self.player.S7, self.player.S8, self.player.S9, self.player.S10]
        for i in slider_position:
            if i == 50:
                don += Constants.slider_value
            else:
                pass
        self.player.donation = don
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
            if self.player.participant.vars['tot_pub_don'] >= Constants.num_rounds / 4:
                self.player.listed = 'YES'
                self.player.name_consent = self.player.participant.vars['name_consent']
                self.player.consent = self.player.participant.vars['consent']
            else:
                self.player.listed = 'NO'

        return {
            'num_rounds': len(self.player.participant.vars['chosen_char']),
            'round_num': round_num,
            'don': self.player.donation

        }


page_sequence = [ShortTask, PostTaskPage]
