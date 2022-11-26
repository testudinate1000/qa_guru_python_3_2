import pytest
from selene.support.shared import SharedConfig, SharedBrowser

BASE_URL = 'https://google.com'


@pytest.fixture
def open_browser():
    config = SharedConfig(window_width=1600, window_height=600)
    browser = SharedBrowser(config)
    return browser.open(BASE_URL)
