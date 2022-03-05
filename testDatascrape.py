from unittest import TestCase


class TestRequestReturnsStatusCode200(TestCase):
    def test_get_web_content(self):
        from dataScrape import get_web_content
        from config import urls
        self.assertEqual(get_web_content(urls['per_game']).status_code, 200)


class TestTableHasContent(TestCase):
    def test_get_table(self):
        from dataScrape import get_table, get_web_content
        from config import urls
        self.assertGreater(len(get_table(get_web_content(urls['per_game']))), 0)


class TestHeadersReturnContent(TestCase):
    def test_get_stat_categories(self):
        from dataScrape import get_table, get_web_content, get_stat_categories
        from config import urls
        stat_cats_text = get_stat_categories(get_table(get_web_content(urls['per_game']))).stat_categories_text
        self.assertGreater(len(stat_cats_text), 0)
        self.assertEqual(stat_cats_text[0], 'Rk')
