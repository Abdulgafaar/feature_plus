from __future__ import unicode_literals

from lettuce import step


@step('I have a client "(.*)"')
def step_x(step, *args):
    assert False
