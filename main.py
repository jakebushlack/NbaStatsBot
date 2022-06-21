import config
import statGetter
import twitterService
from dataScrape import get_and_save
import statToEnglishMapper
from dataService import get_player_data

player_dict = {}

for url in config.urls.keys():

    # get_and_save(config.urls[url])

    player_dict.update(get_player_data(url, player_dict))


def find_top_tens(stats, players):

    top_ten_lists = {}

    for stat in stats:
        top_ten_lists[stat] = get_category_top_ten(stat, players)
    #
    # print(set(top_ten_lists[stats[0]].keys()))
    # print(set(top_ten_lists[stats[1]].keys()))
    # print(set(top_ten_lists[stats[2]].keys()))
    #
    # print(list(set(top_ten_lists[stats[0]].keys()).intersection(set(top_ten_lists[stats[1]].keys())).intersection(set(top_ten_lists[stats[2]].keys()))))
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


custom_attributes = statGetter.remove_default_attributes(player_dict[list(player_dict.keys())[0]])


players_of_interest = []
random_stats = []
while len(players_of_interest) < 1:
    random_stats = statGetter.randomize_attribute(custom_attributes)
    print(random_stats)
    players_of_interest = find_top_tens(random_stats, player_dict)

# outstring = ''
#
# for each_player in players_of_interest:
#     outstring += f'{each_player}, {statToEnglishMapper.statsInEnglish[random_stats[0]]}: {getattr(player_dict[each_player], random_stats[0])}, {statToEnglishMapper.statsInEnglish[random_stats[1]]}: {getattr(player_dict[each_player], random_stats[1])}, {statToEnglishMapper.statsInEnglish[random_stats[2]]}: {getattr(player_dict[each_player], random_stats[2])}\n'


twitterService.generateTweet(player_dict, players_of_interest, random_stats)


