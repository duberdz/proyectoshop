from behave import *

@given(u'Exists a user "user1" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a user "user1" with password "password"')

@given(u'I login as user "user1" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as user "user1" with password "password"')

@when(u'I add product')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I add product')

@then(u'I\'m viewing the details page for restaurant by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for restaurant by "user"')

@then(u'There are 1 product')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 product')

@given(u'I\'m not logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I\'m not logged in')

@then(u'I\'m redirected to the login form')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m redirected to the login form')

@then(u'There are 0 products')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 0 products')