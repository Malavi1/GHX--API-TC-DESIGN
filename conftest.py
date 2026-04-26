import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    # Create a reusable API request context (shared across all tests)
    request_context = playwright.request.new_context()

    yield request_context

    request_context.dispose()  # cleanup after all tests finish

