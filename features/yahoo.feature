Feature: Viewing calendar market data

    User will view the upcoming market events for a given date

    Background: User has logged in
        Given I navigate the login page
        When I enter correct credentials
        Then I should be logged in

    @Calendar
    Scenario: View calendar events for date
        When I click Finance
        And I over hover Market Data
        And I click Calendar
        Then I should see  earnings,stock splits,IPOs and economic events for the given day
            | Date   | earnings | stock splits | IPOs | Economic Events |
            | 14 Mar | 39       | 10           | 2    | 75              |
            | 15 Mar | 54       | 15           | 0    | 114             |