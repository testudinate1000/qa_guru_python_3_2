
from selene import be, have


def test_google_should_find_any_results(open_browser):
    page = open_browser

    page.element('[name=q]').should(be.blank).type('xaf_fwp9NBN4qpn1mfp').press_enter()
    page.element('[id=result-stats]').should(have.text('Результатов: примерно 0'))
