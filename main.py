import config
import statGetter
from dataScrape import get_and_save
from dataService import get_player_data

player_dict = {}

for url in config.urls.keys():

    # get_and_save(config.urls[url])

    player_dict.update(get_player_data(url, player_dict))


def find_top_tens(stats, players):
    # take the three stats of interest
    # take the dictionary of players
    # for each stat, find the top ten players
    # of these top ten players, create a list of the players
    # for each of the players in the list, remove if not found in the other dictionaries

    # top_players = []
    # for stat in stats:
    #     top_players.append(get_category_top_ten(stat, players))

    for stat in stats:
        print(stat)
        print(get_category_top_ten(stat, players))


def get_category_top_ten(stat, players):
    top_ten_dict = {}
    player_objects = list(players.values())

    # for player_obj in player_objects:
    #     print(f'{getattr(player_obj, "player")}: {getattr(player_obj, stat)}')

    players_sorted_descending = sorted(player_objects, key=lambda x: float(getattr(x,  stat)) if getattr(x,  stat) != '' and getattr(x,  stat) is not None else 0, reverse=True)

    for sorted_player in players_sorted_descending[:10]:
        top_ten_dict[getattr(sorted_player, 'player')] = getattr(sorted_player, stat)

    return top_ten_dict


def get_category_bottom_ten(stat, players):
    players_sorted_ascending = list(players).sort(stat)

    return players_sorted_ascending[0:9]


# print(statGetter.remove_default_attributes(player_dict['Jaylen Brown']))

custom_attributes = statGetter.remove_default_attributes(player_dict[list(player_dict.keys())[0]])

random_stats = statGetter.randomize_attribute(custom_attributes)

find_top_tens(random_stats, player_dict)


