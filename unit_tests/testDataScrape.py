import csv
import config
from bs4 import element
from unittest import TestCase
import codecs


class DataScrapeTest(TestCase):
    def test_get_web_content(self):
        from dataScrape import get_web_content
        self.assertEqual(get_web_content(config.urls['totals']).status_code, 200)

    def test_get_table(self):
        from dataScrape import get_table_from_html
        with open(config.test_content['test_html'], "r", encoding="utf-8") as test_html:
            table = get_table_from_html(test_html.read())
            self.assertGreater(len(table), 0)
            self.assertTrue(type(table) == element.Tag)

    def test_save_csv(self):
        from dataScrape import get_table_from_html, save_table_to_csv
        with open(config.test_content['test_html'], 'r', encoding="utf-8") as test_html:
            encoded_html = codecs.encode(test_html.read(), encoding="utf-8")

            table = get_table_from_html(encoded_html)
            save_table_to_csv(table)
            with open('stat_files/test_table.csv', "r", encoding="utf-8") as test_csv:
                csv_reader = list(csv.reader(test_csv, delimiter=','))
                self.assertGreater(len(csv_reader), 0)
