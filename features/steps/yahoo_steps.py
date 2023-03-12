from behave import *
import helpers.helpers as helpers


credentials_file = 'resources/Credentials.xlsx'
crendetials_sheet = 'Credentials'

@given(u'I navigate the login page')
def step_impl(context):
    context.driver_functions.open_page("https://yahoo.com")
    context.driver_functions.find_element_by_name('reject').click()
    context.driver_functions.find_element_by_id('ybarAccountProfile').click()

@given(u'I open financial calendar')
def step_impl(context):
    context.driver_functions.open_page("https://uk.finance.yahoo.com/calendar/")
    context.driver_functions.find_element_by_name('reject').click()

@when(u'I enter correct credentials')
def step_impl(context):
    credentials = helpers.read_xls_file(credentials_file, crendetials_sheet)
    first_row = credentials[0]
    context.driver_functions.find_element_by_id('login-username').send_keys(first_row[0])
    context.driver_functions.find_element_by_id('login-signin').click()
    context.driver_functions.find_element_by_id('login-passwd').send_keys(first_row[1])
    context.driver_functions.find_element_by_id('login-signin').click()

@then(u'I should be logged in')
def step_impl(context):
    assert len(context.driver_functions.find_elements_by_id('ybarAccountMenuOpener')) > 0

@when(u'I click Finance')
def step_impl(context):
    context.driver_functions.find_element_by_id('root_7').click()

@when(u'I over hover Market Data')
def step_impl(context):
    market_data_el = context.driver_functions.find_element_by_xpath('//*[@id="Nav-0-DesktopNav"]/div/div[3]/div/nav/ul/li[2]')
    context.driver_functions.action_hover_element(market_data_el)

@when(u'I click Calendar')
def step_impl(context):
    hidden_calendar_elem = context.driver_functions.find_element_by_xpath(
        '//*[@id="Nav-0-DesktopNav"]/div/div[3]/div/nav/ul/li[2]/div[2]/ul/li[1]/a'
    )
    context.driver_functions.action_move_to_element_and_click(hidden_calendar_elem)

@then(u'I should see  earnings,stock splits,IPOs and economic events for the given day')
def step_impl(context):
    first_date_text = context.driver_functions.find_element_by_xpath(
        '//*[@id="fin-cal-events"]/div[2]/ul/li[1]/div/span[1]').text

    for row in context.table:
        chosen_date_day = row['Date'].split(' ')[0]
        list_index = (int(chosen_date_day) - int(first_date_text)) + 1
        elem_index_in_list = 1
        if int(row['earnings']) > 0:
            earnings_elem = context.driver_functions.find_element_by_xpath(f'//*[@id="fin-cal-events"]/div[2]/ul/li[{list_index}]/a[{elem_index_in_list}]')
            elem_index_in_list += 1
            assert f"{row['earnings']} Earnings" in earnings_elem.text
        if int(row['stock splits']) > 0:
            stock_splits_elem = context.driver_functions.find_element_by_xpath(
                f'//*[@id="fin-cal-events"]/div[2]/ul/li[{list_index}]/a[{elem_index_in_list}]')
            elem_index_in_list += 1
            assert f"{row['stock splits']} Stock splits" in stock_splits_elem.text
        if int(row['IPOs']) > 0:
            ipo_elem = context.driver_functions.find_element_by_xpath(f'//*[@id="fin-cal-events"]/div[2]/ul/li[{list_index}]/a[{elem_index_in_list}]')
            elem_index_in_list += 1
            assert f"{row['IPOs']} IPO pricing" in ipo_elem.text
        if int(row['Economic Events']) > 0:
            economic_events_elem = context.driver_functions.find_element_by_xpath(f'//*[@id="fin-cal-events"]/div[2]/ul/li[{list_index}]/a[{elem_index_in_list}]')
            elem_index_in_list += 1
            assert f"{row['Economic Events']} Economic events" in economic_events_elem.text

