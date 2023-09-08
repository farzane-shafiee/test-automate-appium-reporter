import pytest
from src.apps.reporter_app.tests.logic.search import TestSearch
from src.apps.reporter_app.tests.logic.reporter import TestReporter


@pytest.fixture()
def test_search():
    search_test = TestSearch()
    search_test.setup_class()
    yield search_test


@pytest.fixture()
def test_reporter():
    reporter_test = TestReporter()
    yield reporter_test
