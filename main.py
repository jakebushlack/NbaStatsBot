import config
import statGetter
import twitterService
from dataService import get_player_data

player_dict = {}

for url in config.urls.keys():
    # get_and_save(config.urls[url])
    player_dict.update(get_player_data(url, player_dict))

custom_attributes = statGetter.remove_default_attributes(player_dict[list(player_dict.keys())[0]])

players_of_interest = []
random_stats = []

while len(players_of_interest) < 1:
    random_stats = statGetter.randomize_attribute(custom_attributes)
    players_of_interest = statGetter.find_top_tens(random_stats, player_dict)

twitterService.generate_tweet(player_dict, players_of_interest, random_stats)
