
Feature: View products
  In order to know about the products added to cart
  As a user
  I want to view the products

  Background: products added to cart
    Given Exists a user "user1" with password "password"
    And Exists products added by "user1"
      | usuario       | producto      | pago          |
      | user1         | Champu        | pendiente     |
      | user1         | Coca-cola     | pendiente     |

  Scenario: Remove a product
    Given Exists a user "user1" with password "password"
    Then I can delete product
      | usuario       | producto      | pago          |
      | user1         | Champu        | pagado        |
    And the list shows the remaining products

  Scenario: pay the products
    Given I login as user "user1" with password "password"
    Then I paying the products
      | usuario       | producto      | pago          |
      | user1         | Champu        | pagado        |
    And The list contains the paid products
