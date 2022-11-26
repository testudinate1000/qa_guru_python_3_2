
from selene import be, have


def test_google_should_find_selene(open_browser):
    page = open_browser
    page.element('[name="q"]').should(be.blank).type('selene').press_enter()
    page.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
