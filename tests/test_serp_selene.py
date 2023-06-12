import pytest
from selene import browser
from selene.support.conditions import be, have


@pytest.fixture
def set_window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://google.com')


def test_selene_repo_presented_in_search_results(set_window_size):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_empty_serp(set_window_size):
    browser.element('[name="q"]').should(be.blank).type('vjnfirnijnpqjwnej').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
