import pytest
from src.apps.reporter_app.tests.test_search import TestSearch


@pytest.fixture()
def test_search():
    search_test = TestSearch()
    search_test.setup_class()
    yield search_test
