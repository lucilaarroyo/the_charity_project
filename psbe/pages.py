from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SIS(Page):
    form_model = 'player'
    form_fields = ['future','email', 'SIS']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'part_pool': self.player.participant.vars['part_pool']

        }

    def before_next_page(self):
        if self.player.SIS == 0:
            self.player.participant.vars['end_experiment'] = True
        else:
            pass


class TY2(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1 and self.participant.vars['end_experiment'] == True

    def vars_for_template(self):
        return {

        }


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'part_pool': self.player.participant.vars['part_pool']

        }


class Dem(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'ethnicity', 'race']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {

        }


# class Subc(Page):
#     form_model = 'player'
#     form_fields = ['SubC1', 'SubC2', 'SubC3', 'SubC4', 'SubC5', 'SubC6', 'SubC7', 'SubC8', 'SubC9', 'SubC10']
#
#     def is_displayed(self):
#         return self.subsession.round_number == 1
#
#     def vars_for_template(self):
#         return {
#             'SubC_num': self.player.participant.vars['orderSubC'],
#         }


class SCA1(Page):
    form_model = 'player'
    form_fields = ['sh1', 'sh2', 'g1', 'g2', 'd1', 'd2', 'e1', 'e2']

    def is_displayed(self):
        orderscapages = self.player.participant.vars['orderSCApages']
        return self.subsession.round_number == (orderscapages.index('SCA1') + 1)

    def vars_for_template(self):
        return {
            'SCA': self.player.participant.vars['orderSCA1'],
            'oscap': self.player.participant.vars['orderSCApages'],
            'round_num': self.subsession.round_number
        }


class SCA2(Page):
    form_model = 'player'
    form_fields = ['sh3', 'sh4', 'g3', 'g4', 'd3', 'd4', 'e3', 'e4']

    def is_displayed(self):
        orderscapages = self.player.participant.vars['orderSCApages']
        return self.subsession.round_number == (orderscapages.index('SCA2') + 1)

    def vars_for_template(self):
        return {
            'SCA': self.player.participant.vars['orderSCA2'],
            'oscap': self.player.participant.vars['orderSCApages'],
            'round_num': self.subsession.round_number
        }


class SCA3(Page):
    form_model = 'player'
    form_fields = ['sh5', 'sh6', 'g5', 'g6', 'd5', 'd6', 'e5', 'e6']

    def is_displayed(self):
        orderscapages = self.player.participant.vars['orderSCApages']
        return self.subsession.round_number == (orderscapages.index('SCA3') + 1)

    def vars_for_template(self):
        return {
            'SCA': self.player.participant.vars['orderSCA3'],
            'oscap': self.player.participant.vars['orderSCApages'],
            'round_num': self.subsession.round_number
        }


class SCA4(Page):
    form_model = 'player'
    form_fields = ['sh7', 'sh8', 'g7', 'g8', 'd7', 'd8', 'e7', 'e8']

    def is_displayed(self):
        orderscapages = self.player.participant.vars['orderSCApages']
        return self.subsession.round_number == (orderscapages.index('SCA4') + 1)

    def vars_for_template(self):
        return {
            'SCA': self.player.participant.vars['orderSCA4'],
            'oscap': self.player.participant.vars['orderSCApages'],
            'round_num': self.subsession.round_number
        }


class SCA5(Page):
    form_model = 'player'
    form_fields = ['sh9', 'sh10', 'g9', 'g10', 'd9', 'd10', 'e9', 'e10']

    def is_displayed(self):
        orderscapages = self.player.participant.vars['orderSCApages']
        return self.subsession.round_number == (orderscapages.index('SCA5') + 1)

    def vars_for_template(self):
        return {
            'SCA': self.player.participant.vars['orderSCA5'],
            'oscap': self.player.participant.vars['orderSCApages'],
            'round_num': self.subsession.round_number
        }


class SCA6(Page):
    form_model = 'player'
    form_fields = ['sh11', 'g11', 'd11', 'e11']

    def is_displayed(self):
        orderscapages = self.player.participant.vars['orderSCApages']
        return self.subsession.round_number == (orderscapages.index('SCA6') + 1)

    def vars_for_template(self):
        return {
            'oscap': self.player.participant.vars['orderSCApages'],
            'round_num': self.subsession.round_number

        }


class IntroTask1(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):

        return {
            'num_paired_dot_rounds': Constants.num_paired_dot_rounds,
            'round_multiplier': Constants.round_multiplier,
            'dots_secs': Constants.dots_secs,
            'num_dots_easy': Constants.num_dots_easy,
            'num_dots_hard': Constants.num_dots_hard,
            'part_pool': self.player.participant.vars['part_pool'],

        }


page_sequence = [
    SIS,
    TY2,
    Introduction,
    Dem,
    SCA1,
    SCA2,
    SCA3,
    SCA4,
    SCA5,
    SCA6,
    IntroTask1,
]
