from unittest import TestCase

import config


class TestRequestReturnsStatusCode200(TestCase):
    def test_get_web_content(self):
        from dataScrape import get_web_content
        from config import urls
        self.assertEqual(get_web_content(urls['per_game']).status_code, 200)


class TestTableHasContent(TestCase):
    def test_get_table(self):
        from dataScrape import get_table
        with open(config.test_content, encoding='UTF-8') as test_file:
            self.assertGreater(len(str(get_table(test_file))), 0)


class TestTableSavedToCsv(TestCase):
    def test_file_saved(self):
        from dataScrape import get_table, get_web_content, save_table_to_csv
        from config import urls
        save_table_to_csv(get_table(config.test_content))
        self.assertGreater(len(get_table(get_web_content(urls['per_game']))), 0)