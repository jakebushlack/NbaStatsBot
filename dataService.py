import csv

import config
from Player import Player

player_dict = {"": ""}


def get_player_data(_file_name, _player_dict):
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


def new_get_player_data(_player_dict):

    for file_name in config.urls.keys():

        with open((file_name + "_stats.csv"), encoding='UTF-8') as stats_file:
            csv_reader = list(csv.reader(stats_file, delimiter=','))
            header = csv_reader[0]
            row_index = 1

            for row in csv_reader:
                col_index = 0
                player = Player(header[col_index], row[col_index])  # create player object initialized by the player's name
                player_name = getattr(player, 'player')

                if not _player_dict[player_name]:  # if we can't find this row's player obj by key in the player dictionary

                    for stat in row:
                        player.adding_new_attr(header[col_index], stat)  # add the rest of the stats from the row to the current player obj
                        col_index += 1

                    player_dict[player_name] = player  # add the current player and all of their stats to the player dictionary
                    continue

                player_dict_value = _player_dict[player_name]

                for stat in row:
                    if not player_dict_value == 'null':  # if the attribute doesn't exist on the player object
                        player_dict_value.adding_new_attr(header[col_index], stat)
                        player_dict_value.adding_new_attr(header[col_index], stat)
                    col_index += 1

                player_dict[player_name] = player_dict_value

                row_index += 1

# get_player_data("stat_files/per_game_stats")
