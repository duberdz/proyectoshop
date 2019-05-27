Feature: List Products
  In order to keep myself up to date about the products registered in shoponline
  As a user

  Background: There are 5 registered products by same user
    Given Exists a user "admin" with password "password"
    And Exists products registered by "admin"
      | nombre          | precio      | categoria     |
      | Patata          | 1.75        | Ortaliza      |
      | Manzana         | 2.20        | Fruta         |
      | Champu          | 3.50        | Higiene       |
      | Coca-cola       | 1.70        | Bebidas       |
      | Chorizo         | 2.30        | Embutidos     |


  Scenario: List products
    Given Exists products registered by "admin"
      | nombre          | precio      | categoria     |
      | Patata          | 1.75        | Ortaliza      |
    When I list products
    Then I'm viewing a list containing
      | nombre          | precio      | categoria     |
      | Patata          | 1.75        | Ortaliza      |
      | Manzana         | 2.20        | Fruta         |
      | Champu          | 3.50        | Higiene       |
      | Coca-cola       | 1.70        | Bebidas       |
      | Chorizo         | 2.30        | Embutidos     |
