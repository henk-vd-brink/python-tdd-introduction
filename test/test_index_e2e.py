import unittest
from selenium import webdriver


class E2ETests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000/")

    def tearDown(self) -> None:
        self.driver.close()

    def test_browser_title_contains_app_name(self) -> None:
        self.assertIn("Named Entity Finder", self.driver.title)

    def test_page_heading_is_named_entity_finder(self) -> None:
        heading = self._find("heading")
        self.assertEqual("Named Entity Finder", heading.text)

    def test_page_has_input_for_text(self) -> None:
        input_element = self._find("input-text")
        self.assertIsNotNone(input_element)

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')
