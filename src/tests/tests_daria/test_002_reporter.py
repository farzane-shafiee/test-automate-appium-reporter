import time
import pytest
from src.tests.conftest import BaseTest
from src.page.report_page.reporter_page import ReporterPage


class TestReporter(BaseTest):
    test_dependencies = [
        "test_001_search.py::TestSearch::test_01_searches",
    ]

    @pytest.mark.dependency(
            depends=test_dependencies,
            scope='session'
        )
    def test_02_reporters(self):

        reporter_page = ReporterPage(self.driver)

        time.sleep(5)
        reporter_page.click_report_type_dropdown()
        time.sleep(2)


