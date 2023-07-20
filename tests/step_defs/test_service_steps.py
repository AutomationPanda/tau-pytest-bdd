"""
This module contains step definitions for service.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests

from pytest_bdd import scenarios, given, then, parsers


# Shared Variables

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'


# Scenarios


scenarios('../features/service.feature')

CONVERTERS = {
  'code': int,
  'phrase': str,
}


# Given Steps

@given(
  parsers.parse('the DuckDuckGo API is queried with "{phrase}"'),
  target_fixture='ddg_response',
  converters=CONVERTERS)
def ddg_response(phrase):
  params = {'q': phrase, 'format': 'json'}
  response = requests.get(DUCKDUCKGO_API, params=params)
  return response


# Then Steps

@then(
  parsers.parse('the response contains results for "{phrase}"'),
  converters=CONVERTERS)
def ddg_response_contents(ddg_response, phrase):
  # A more comprehensive test would check 'RelatedTopics' for matching phrases
  assert phrase.lower() == ddg_response.json()['Heading'].lower()


@then(
  parsers.parse('the response status code is "{code}"'),
  converters=CONVERTERS)
def ddg_response_code(ddg_response, code):
  assert ddg_response.status_code == code
