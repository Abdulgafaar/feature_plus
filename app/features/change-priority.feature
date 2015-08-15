Feature: Test that a client's Feature.priority can be re-ordered correctly

  Scenario: Test priority re-order
    Given I have a client "Client A"
    When a new feature for product "Policies" with priority "1" is created
    Then I confirm I have a feature

    But the client requested a new feature for product "Billing" with priority "1"
    When I have created this new feature
    Then I confirm I have 2 features
    And the feature with priority 1 is "Billing"
