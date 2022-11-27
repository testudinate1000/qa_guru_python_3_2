
import pytest
from selene.support.shared import SharedConfig, SharedBrowser

BASE_URL = 'https://google.com'


@pytest.fixture
def open_browser():
    config = SharedConfig(window_width=1920, window_height=1080)
    browser = SharedBrowser(config)
    return browser.open(BASE_URL)
