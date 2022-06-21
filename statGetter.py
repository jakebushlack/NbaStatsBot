from random import randint
import config
from dataService import get_player_data


def randomize_attribute(custom_player_attributes):
    selected_attributes = []
    while len(selected_attributes) < 3:
        rand_index = randint(0, len(custom_player_attributes))
        if custom_player_attributes[rand_index] not in selected_attributes:
            selected_attributes.append(custom_player_attributes[rand_index])
    return selected_attributes


def remove_default_attributes(player):

    all_player_attributes = list(dir(player))
    custom_player_attributes = []
    stats_that_arent_stats = ['player', 'stats', 'team_id', 'adding_new_attr', '', 'pos']

    for thing in all_player_attributes:
        if not thing.endswith("__") and thing not in stats_that_arent_stats:
            custom_player_attributes.append(thing)

    return custom_player_attributes


player_dict = {}

for url in config.urls.keys():
    player_dict.update(get_player_data(url, player_dict))

