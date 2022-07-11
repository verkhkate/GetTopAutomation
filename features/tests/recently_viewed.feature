Feature: TESTS FOR "RECENTLY VIEWED"

  @smoke
  Scenario: User can see recently viewed items, open them and is taken to correct page
    Given Open GetTop website home page
    Then Verify that GetTop website home page is opened
    When Click on "IPHONE" category in the Header menu
    Then Verify that "IPHONE" category page is opened
#    When Click on any product
#    Then Verify that correct product page is opened
#    When Click on "WATCH" category in the Header menu
#    Then Verify that "WATCH" category page is opened
#    Then Verify that "RECENTLY VIEWED" section is visible on the page
#    When Click on the product in "RECENTLY VIEWED" section
#    Then Verify that correct product page is opened
