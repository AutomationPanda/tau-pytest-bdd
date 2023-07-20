@web @duckduckgo
Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.


  Background:
    Given the DuckDuckGo home page is displayed


  Scenario: Basic DuckDuckGo Search
    When the user searches for "panda"
    Then results are shown for "panda"


  Scenario: Lengthy DuckDuckGo Search
    When the user searches for the phrase:
      """
      When in the Course of human events, it becomes necessary for one people
       to dissolve the political bands which have connected them with another,
       and to assume among the powers of the earth, the separate and equal
       station to which the Laws of Nature and of Nature's God entitle them,
       a decent respect to the opinions of mankind requires that they should
       declare the causes which impel them to the separation.
      """
    Then one of the results contains "Declaration of Independence"