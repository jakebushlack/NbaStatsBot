import csv

import config
from Player import Player

player_dict = {"": ""}

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
            print(getattr(player, 'player'))
            for stat in row:
                player.adding_new_attr(header[column_count], stat)
                column_count += 1
            players.append(player)
            player_dict[getattr(player, 'player')] = player
            row_count += 1


def join_player_data(_player, _header, _stats):
    # for each stat, check the existing player object for existing stats and skip.
    # for unique/new stats, add to player
    for stat in _stats:
        if not getattr(_player, stat, 'null') == 'null':
            _player.adding_new_attr(_header.value, stat.value)

    for file_name in config.urls.keys():
        with open((file_name + "_stats.csv"), encoding='UTF-8') as stats_file:
            csv_reader = list(csv.reader(stats_file, delimiter=','))
            header = csv_reader[0]



# get_player_data("stat_files/per_game_stats")
