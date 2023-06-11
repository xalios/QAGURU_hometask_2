from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_selene_repo_presented_in_search_results(browser_chrome):
    expected_text = 'User-oriented Web UI browser tests in Python'
    browser = browser_chrome
    search_form = browser.find_element(By.NAME, "q")
    search_form.send_keys('selene')
    search_form.send_keys(Keys.ENTER)
    serp_text = browser.find_element(By.ID, "search").text
    assert expected_text in serp_text, 'Expected text not found in search results'


def test_empty_serp(browser_chrome):
    browser = browser_chrome
    search_form = browser.find_element(By.NAME, "q")
    search_form.send_keys('vjnfirnijnpqjwnej')
    search_form.send_keys(Keys.ENTER)
    serp_text = browser.find_element(By.ID, "search").text
    assert len(serp_text) == 0, f'Serp element is not empty'




