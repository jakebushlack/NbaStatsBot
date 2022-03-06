from unittest import TestCase
from config import test_content


test_file = open(test_content)

class TestFindStatsTable(TestCase):
    def test_get_stat_categories(self):
        from dataScrape import get_web_content
        from config import urls
        self.assertEqual(get_web_content(urls['per_game']).status_code, 200)


