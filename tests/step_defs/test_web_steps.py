"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:
 - Firefox must be installed.
 - geckodriver must be installed and accessible on the system path.
"""

from pytest_bdd import scenarios, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Scenarios

scenarios('../features/web.feature')


# When Steps

@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    search_input = browser.find_element(By.NAME, 'q')
    search_input.send_keys(text + Keys.RETURN)


# Then Steps

@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//*[@data-testid='result']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements(By.XPATH, xpath)
    assert len(results) > 0


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    assert len(browser.find_elements(By.CSS_SELECTOR, '[data-testid="result"]')) > 0
    # Check search phrase
    search_input = browser.find_element(By.NAME, 'q')
    assert search_input.get_attribute('value') == phrase
