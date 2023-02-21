from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import CucumberBasket


EXTRA_TYPES = {
    'Number': int,
}


CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}


scenarios('../features/cucumbers.feature')


# @given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture='basket')
@given('the basket has "{initial}" cucumbers', target_fixture='basket',converters=CONVERTERS)
def basket(initial):
    return CucumberBasket(initial_count=initial)


# @when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
@when('"{some}" cucumbers are added to the basket',converters=CONVERTERS)
def add_cucumbers(basket, some):
    basket.add(some)


# @when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
@when('"{some}" cucumbers are removed from the basket',converters=CONVERTERS)
def remove_cucumbers(basket, some):
    basket.remove(some)


# @then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
@then('the basket contains "{total}" cucumbers',converters=CONVERTERS)
def basket_has_total(basket, total):
    assert basket.count == total
