from ast import And, Return
from pytest_bdd import scenario, given, when, then, parsers

from cucumbers import CucumberBasket
import re

@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=dict(Number=int)), target_fixture="basket")    
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=dict(Number=int)))
def add_cucumbers(basket, some):
   basket.add(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=dict(Number=int)))
def basket_has_total(basket, total):
    assert basket.count == total