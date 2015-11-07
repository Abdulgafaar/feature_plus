from __future__ import unicode_literals, absolute_import

from lettuce import step


@step('I have a client "(.*)"')
def step_x(step, *args):
    assert False
