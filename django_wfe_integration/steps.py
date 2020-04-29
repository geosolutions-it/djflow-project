from time import sleep
from random import randint
from django_wfe import steps


class StepA(steps.Step):

    def execute(self, _input=None, *args, **kwargs):
        sleep(3)
        return randint(0, 1)


class Decision(steps.Decision):

    def transition(self, _input=None, *args, **kwargs):
        sleep(3)
        return _input


class StepB(steps.Step):

    def execute(self, _input=None, *args, **kwargs):
        sleep(3)


class StepC(steps.Step):

    def execute(self, _input=None, *args, **kwargs):
        sleep(3)
