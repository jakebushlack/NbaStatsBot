import csv
import types

import config
from StatCategories import StatCategories
from Player import Player


def get_stat_categories(_file_name):
    stat_categories = StatCategories()

    if len(_file_name) > 0:
        header = _file_name.find("thead").find("tr").select("[aria-label]")
        for col in header:
            stat_categories.stat_categories_text.append(col.text)
            stat_categories.stat_categories_concise.append(col['data-stat'])
            stat_categories.stat_categories_verbose.append(col['aria-label'])

            print('"' + str(col['data-stat']) + '"' + ": " + '"' + str(col['aria-label']) + '"')

    return stat_categories


def get_player_data(_file_name):
    players = []
    with open(_file_name, encoding='UTF-8') as stats_file:
        csv_reader = list(csv.reader(stats_file, delimiter=','))
        header = csv_reader[0]
        row_count = 0
        for row in csv_reader:
            column_count = 0
            if row_count == 0:
                row_count += 1
                continue
            player = Player(header[column_count], row[column_count])
            print(player.player)
            for stat in row:
                player.adding_new_attr(header[column_count], stat)
                column_count += 1
            players.append(player)
            row_count += 1
        print(header)


def join_player_data(_player, _header, _stats):
    # for each stat, check the existing player object for existing stats and skip.
    # for unique/new stats, add to player
    for stat in _stats:
        if not getattr(_player, stat, 'null') == 'null':
            _player.adding_new_attr(_header.value, stat.value)
    return []


get_player_data("stat_files/per_game_stats")
