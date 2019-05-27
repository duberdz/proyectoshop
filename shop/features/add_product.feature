Feature: add product
  In order to add a new product to cart
  As a user
  I want to add the product at a list to buy

  Background: There is a registered user
    Given Exists a user "user1" with password "password"

  Scenario: add the product
    Given I login as user "user1" with password "password"
    When I add product
      | usuario       | producto      | pago          |
      | user          | Champu        | pendiente     |
    Then I'm viewing the details page for restaurant by "user"
      | usuario       | producto      | pago          |
      | user          | Champu        | pendiente     |
    And There are 1 product

  Scenario: Try to add product but not logged in
    Given I'm not logged in
    When I add product
      | usuario       | producto      | pago          |
      | user          | Champu        | pendiente     |
    Then I'm redirected to the login form
    And There are 0 products