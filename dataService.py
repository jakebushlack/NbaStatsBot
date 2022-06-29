import csv
import logging

from Player import Player


def get_player_data(_file_name, _player_dict):

    with open(f'stat_files/{_file_name}_stats.csv', encoding='UTF-8') as stats_file:

        logging.debug(f'Merging data from {_file_name}')

        csv_reader = list(csv.reader(stats_file, delimiter=','))
        header = csv_reader[0]
        row_index = 0

        for row in csv_reader:

            if row_index == 0:
                row_index += 1
                continue

            col_index = 0
            player = Player(header[col_index], row[col_index])  # create player object initialized by the player's name
            player_name = getattr(player, 'player')

            if not _player_dict.get(player_name):  # if we can't find this row's player obj by key in the player dictionary

                logging.debug(f'Adding new player {player_name} to player dictionary')

                for stat in row:
                    player.adding_new_attr(header[col_index], stat)  # add the rest of the stats from the row to the current player obj
                    col_index += 1

                _player_dict[player_name] = player  # add the current player and all of their stats to the player dictionary
                continue

            player_dict_value = _player_dict.get(player_name)

            for stat in row:
                if not player_dict_value == 'null':  # if the attribute doesn't exist on the player object
                    player_dict_value.adding_new_attr(header[col_index], stat)
                col_index += 1

            _player_dict[player_name] = player_dict_value

            row_index += 1

    logging.debug(f'Number of attributes on each player: {len(dir(_player_dict[list(_player_dict.keys())[0]]))}')

    return _player_dict



