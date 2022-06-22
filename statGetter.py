from random import randint


def randomize_attribute(custom_player_attributes):
    selected_attributes = []

    while len(selected_attributes) < 3:
        rand_index = randint(0, len(custom_player_attributes) - 1)

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


def find_top_tens(stats, players):
    top_ten_lists = {}

    for stat in stats:
        top_ten_lists[stat] = get_category_top_ten(stat, players)

    return list(set(top_ten_lists[stats[0]].keys()).intersection(set(top_ten_lists[stats[1]].keys())).intersection(set(top_ten_lists[stats[2]].keys())))


def get_category_top_ten(stat, players):
    top_ten_dict = {}
    player_objects = list(players.values())
    players_sorted_descending = sorted(player_objects, key=lambda x: float(getattr(x,  stat)) if getattr(x,  stat) != '' and getattr(x,  stat) is not None else 0, reverse=True)

    for sorted_player in players_sorted_descending[:10]:
        top_ten_dict[getattr(sorted_player, 'player')] = getattr(sorted_player, stat)

    return top_ten_dict


def get_category_bottom_ten(stat, players):
    players_sorted_ascending = list(players).sort(stat)

    return players_sorted_ascending[0:9]

