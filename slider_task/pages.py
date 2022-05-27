from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class ShortTask(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['S1', 'S2', 'S3', 'S4', 'S5']

    def is_displayed(self):
        return self.subsession.round_number <= self.player.participant.vars['chosen_tasks_committed'] and \
               self.participant.vars['end_experiment'] is False

    def vars_for_template(self):
        round_num = self.subsession.round_number

        self.player.charity = self.player.participant.vars['chosen_charity']
        self.player.anonymity = self.player.participant.vars['chosen_anonymity']
        self.player.matched_donation = self.player.participant.vars['matchedDonation']

        for_marg = range(0, 570+1, 10)
        marg = random.sample(for_marg, k=5)

        return {
            'num_rounds': self.player.participant.vars['chosen_tasks_committed'],
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
        self.player.participant.vars['total_don'] += self.player.donation
        if self.player.anonymity == "Public":
            self.player.participant.vars['tot_pub_don'] += self.player.donation
        else:
            self.player.participant.vars['tot_anon_don'] += self.player.donation


# class TasksWaitPage(WaitPage):
#     def is_displayed(self):
#         return self.subsession.round_number <= len(self.player.participant.vars['chosen_char']) and \
#                self.participant.vars['end_experiment'] is False


class PostTaskPage(Page):
    def is_displayed(self):
        return self.subsession.round_number <= self.player.participant.vars['chosen_tasks_committed'] and \
               self.participant.vars['end_experiment'] is False

    def vars_for_template(self):
        round_num = self.subsession.round_number
        if round_num == self.player.participant.vars['chosen_tasks_committed']:
            if self.player.participant.vars['tot_pub_don'] >= (Constants.num_rounds / 2):
                self.player.listed = 'YES'
            else:
                self.player.listed = 'NO'

            self.player.total_pub_don = self.player.participant.vars['tot_pub_don']
            self.player.total_anon_don = self.player.participant.vars['tot_anon_don']

        return {
            'num_rounds': self.player.participant.vars['chosen_tasks_committed'],
            'round_num': round_num,
            'don': self.player.donation,
            'donated_so_far_pub': self.player.participant.vars['tot_pub_don'],
            'donated_so_far_anon': self.player.participant.vars['tot_anon_don'],
            'total_don': self.player.participant.vars['total_don'],
            'charity': self.player.charity,

        }


page_sequence = [ShortTask, PostTaskPage]
