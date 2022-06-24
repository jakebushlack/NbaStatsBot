import csv
from unittest import TestCase
from dataService import get_player_data
import config
from config import test_content

test_file = test_content['test_table']


class TestFindStatsTable(TestCase):
    def test_open_test_csv(self):
        with open(test_file, encoding='UTF-8') as test_csv:
            self.assertGreater(len(test_csv.readlines()), 0)

    def test_find_stats_table(self):
        player_dict = get_player_data('test_table', {})
        self.assertGreater(len(player_dict), 0)
        self.assertTrue(type(player_dict) is dict)

    def test_remove_duplicate_stat_categories(self):
        stats_count = 0
        for file_name in config.urls:
            with open(f'stat_files/{file_name}_stats.csv', encoding='UTF-8') as stats_file:
                csv_reader = list(csv.reader(stats_file, delimiter=','))
                stats_count += len(csv_reader[0])
        self.assertLess(len(dir(get_player_data('test_table', {})['Marcus Smart'])), stats_count)

