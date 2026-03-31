Feature: Connected Systems - Inventory to Storefront

    Scenario: Create inventory item via API and complete purchase in UI
        Given I create a new pet in the inventory system
        When I login to the storefront
        And I add a product to the cart
        And I checkout using data from the created pet
        Then the order should be successfully placed