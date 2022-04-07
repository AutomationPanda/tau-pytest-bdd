Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.


  Scenario: Add cucumbers to a basket
    Given the basket has "2" cucumbers
    When "4" cucumbers are added to the basket
    Then the basket contains "6" cucumbers

  Scenario: Add some other cucumbers to a basket
    Given the basket has "5" cucumbers
    When "4" cucumbers are added to the basket
    Then the basket contains "9" cucumbers

 Scenario: Remove some cucumbers
    Given the basket has "10" cucumbers
    When "4" cucumbers are removed from the basket
    Then the basket contains "6" cucumbers
