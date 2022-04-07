from ast import And, Return
from pytest_bdd import scenarios, given, when, then, parsers

from cucumbers import CucumberBasket
import re

scenarios('../features/cucumbers.feature')

EXTRA_TYPES = {
    'Number' : int,
}

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture="basket")    
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
def add_cucumbers(basket, some):
   basket.add(some)

@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket, some):
   basket.remove(some)

@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total