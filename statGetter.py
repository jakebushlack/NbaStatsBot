from random import randint
import config
from dataService import get_player_data


def randomize_attribute(custom_player_attributes):
    selected_attributes = []
    while len(selected_attributes) < 3:
        rand_index = randint(0, len(custom_player_attributes))
        selected_attributes.append(custom_player_attributes[rand_index])
    return selected_attributes


def remove_default_attributes(player):
    print("hi")

    all_player_attributes = list(dir(player))
    custom_player_attributes = []
    print(f'len of dict list {len(all_player_attributes)}')

    for thing in all_player_attributes:
        if not thing.endswith("__") and not len(thing) < 1 and not thing.endswith("adding_new_attr"):
            custom_player_attributes.append(thing)

    print(f'len of dict list {len(custom_player_attributes)}')

    return custom_player_attributes


player_dict = {}

for url in config.urls.keys():
    player_dict.update(get_player_data(url, player_dict))

