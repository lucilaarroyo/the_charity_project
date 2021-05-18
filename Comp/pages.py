from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'compensation': Constants.compensation,
            'endowment': Constants.endowment,
        }


class WEW1(Page):
    form_model = 'player'
    form_fields = ['WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11',
                   'WEW12', 'WEW13', 'WEW14']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'WEW1_num': self.player.participant.vars['orderWEW1'],
        }


class WEW2(Page):
    form_model = 'player'
    form_fields = ['WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11',
                   'WEW12', 'WEW13', 'WEW14']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities

    def vars_for_template(self):
        return {
            'WEW1_num': self.player.participant.vars['orderWEW2'],
        }


class WEW3(Page):
    form_model = 'player'
    form_fields = ['WEW1', 'WEW2', 'WEW3', 'WEW4', 'WEW5', 'WEW6', 'WEW7', 'WEW8', 'WEW9', 'WEW10', 'WEW11',
                   'WEW12', 'WEW13', 'WEW14']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'WEW1_num': self.player.participant.vars['orderWEW3'],
        }


class SubC(Page):
    form_model = 'player'
    form_fields = ['SubC1', 'SubC2', 'SubC3', 'SubC4', 'SubC5', 'SubC6', 'SubC7', 'SubC8', 'SubC9', 'SubC10']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'SubC_num': self.player.participant.vars['orderSubC'],
        }


class SAQ(Page):
    form_model = 'player'
    form_fields = ['SAQ1', 'SAQ2', 'SAQ3', 'SAQ4', 'SAQ5', 'SAQ6', 'SAQ7', 'SAQ8', 'SAQ9', 'SAQ10']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'SAQ_num': self.player.participant.vars['orderSAQ'],
        }


class InstructionsFT(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class FirstTask(Page):
    form_model = 'player'
    form_fields = ['deservingness', 'closeness']

    def is_displayed(self):
        return self.subsession.round_number <= Constants.num_charities

    def vars_for_template(self):
        charity_num = self.subsession.round_number
        self.player.charity_task_1 = self.player.participant.vars['orderTask1'][(charity_num-1)]

        return {
            'charity_num': charity_num,
            'last_charity': Constants.num_charities,
            'charity': self.player.charity_task_1,
            #'image_path_pic': 'Comp/pics/{} pic.jpg'.format(self.player.charity_task_1),
            #'image_path_mission': 'Comp/pics/{} mission.jpg'.format(self.player.charity_task_1),
            'image_path_info': 'Comp/pics/{}.jpg'.format(self.player.charity_task_1),
        }


class InstructionsST(Page):
    form_model = 'player'
    form_fields = ['consent']

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_charities

    def vars_for_template(self):
        return {
            'endowment': Constants.endowment,
        }


class SecondTask(Page):
    form_model = 'player'
    form_fields = ['donation']

    def is_displayed(self):
        return self.subsession.round_number >= Constants.num_charities

    def vars_for_template(self):
        round_num = self.subsession.round_number - Constants.num_charities + 1
        self.player.anonymity_task_2 = self.player.participant.vars['dictAnonym'][(round_num-1)]
        self.player.charity_task_2 = self.player.participant.vars['orderTask2'][(round_num-1)]

        return {
            'num_rounds': Constants.num_rounds,
            'val_endowment': Constants.val_endowment,
            'round_num': round_num,
            'anonymity': self.player.anonymity_task_2,
            'charity': self.player.charity_task_2,
            'image_path_info': 'Comp/pics/{} short.jpg'.format(self.player.charity_task_2),
        }

    def before_next_page(self):
        self.player.set_payoffs()
        #round_num = self.subsession.round_number - Constants.num_charities + 1
        # charity_and_version = self.player.participant.vars['dictVersion'][(round_num - 1)]
        # version = charity_and_version[1]
        # if version == 1:
        #     self.player.participant.vars['version_1_count'] += 1


class ChD(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.payment_round = self.player.participant.vars['payRound']
        self.player.chosen_charity = self.player.in_round(self.player.payment_round).charity_task_2
        self.player.chosen_anonymity = self.player.in_round(self.player.payment_round).anonymity_task_2
        self.player.subject_donation = self.player.in_round(self.player.payment_round).donation

        if self.player.chosen_anonymity == "ANONYMOUS":
            self.player.listed = 'NO'
        else:
            if self.player.subject_donation >= Constants.val_endowment/2:
                self.player.listed = 'YES'
            else:
                self.player.listed = 'NO'

        if self.player.chosen_anonymity == "PUBLIC":
            self.player.matched_donation = 'NO'
        else:
            self.player.matched_donation = self.player.participant.vars['matchedDonation'][0]

        return {
            'charity': self.player.chosen_charity,
            'anonymity': self.player.chosen_anonymity,
            'subject_donation': self.player.subject_donation,
            'listed': self.player.listed,
            'matched_donation': self.player.matched_donation,
        }


class ThankYou(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        payment_round = self.player.participant.vars['payRound']
        self.player.endow_portion = self.player.in_round(payment_round).payoff

        if self.player.in_round(Constants.num_rounds).matched_donation == 'YES':
            self.player.total_donation = self.player.in_round(Constants.num_rounds).subject_donation * 2
        else:
            self.player.total_donation = self.player.in_round(Constants.num_rounds).subject_donation

        self.player.total_subject_payoff = Constants.compensation + self.player.endow_portion

        return {
            'charity': self.player.in_round(Constants.num_rounds).chosen_charity,
            'anonymity': self.player.in_round(Constants.num_rounds).chosen_anonymity,
            'subject_donation': self.player.in_round(Constants.num_rounds).subject_donation,
            'endow_portion': self.player.endow_portion,
            'matched_donation': self.player.in_round(Constants.num_rounds).matched_donation,
            'total_donation': self.player.total_donation,
            'endowment': Constants.endowment,
            'compensation': Constants.compensation,
            'total_subject_payoff': self.player.total_subject_payoff,
            'listed': self.player.in_round(Constants.num_rounds).listed,

        }


page_sequence = [
    # Introduction,
    WEW1,
    # SubC,
    # SAQ,
    # InstructionsFT,
    FirstTask,
    # WEW2,
    InstructionsST,
    SecondTask,
    ChD,
    # WEW3,
    ThankYou,
]
