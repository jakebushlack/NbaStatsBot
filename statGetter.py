
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
    bottom_ten_dict = {}
    player_objects = list(players.values())
    players_sorted_ascending = sorted(player_objects, key=lambda x: float(getattr(x,  stat)) if getattr(x,  stat) != '' and getattr(x,  stat) is not None else 0)

    for sorted_player in players_sorted_ascending[:10]:
        bottom_ten_dict[getattr(sorted_player, 'player')] = getattr(sorted_player, stat)

    return bottom_ten_dict

