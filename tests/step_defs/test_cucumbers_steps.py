from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import CucumberBasket


scenarios('../features/cucumbers.feature')


CONVERTERS = {
  'initial': int,
  'some': int,
  'total': int,
}


@given(
  parsers.parse('the basket has "{initial}" cucumbers'),
  target_fixture='basket',
  converters=CONVERTERS)
def basket(initial):
  return CucumberBasket(initial_count=initial)


@when(
  parsers.parse('"{some}" cucumbers are added to the basket'),
  converters=CONVERTERS)
def add_cucumbers(basket, some):
  basket.add(some)


@when(
  parsers.parse('"{some}" cucumbers are removed from the basket'),
  converters=CONVERTERS)
def remove_cucumbers(basket, some):
  basket.remove(some)


@then(
  parsers.parse('the basket contains "{total}" cucumbers'),
  converters=CONVERTERS)
def basket_has_total(basket, total):
  assert basket.count == total
