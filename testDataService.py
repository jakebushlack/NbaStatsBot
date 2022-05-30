import csv
from unittest import TestCase

import config
from config import test_content

test_file = test_content['test_csv']


class TestFindStatsTable(TestCase):
    def test_find_stats_table(self):
        from dataService import get_player_data
        self.assertGreater(len(get_player_data({})), 0)

    def test_remove_duplicate_stat_categories(self):
        from dataService import get_player_data
        stats_count = 0
        for file_name in config.urls:
            with open(f'stat_files/{file_name}_stats.csv', encoding='UTF-8') as stats_file:
                csv_reader = list(csv.reader(stats_file, delimiter=','))
                stats_count += len(csv_reader[0])
        self.assertLess(len(dir(get_player_data({})['Marcus Smart'])), stats_count)

    def test_remove_duplicate_stat_categories(self):
        from dataService import get_player_data
        stats_count = 0
        for file_name in config.urls:
            with open(f'stat_files/{file_name}_stats.csv', encoding='UTF-8') as stats_file:
                csv_reader = list(csv.reader(stats_file, delimiter=','))
                stats_count += len(csv_reader[0])
        self.assertLess(len(dir(get_player_data({})['Marcus Smart'])), stats_count)

