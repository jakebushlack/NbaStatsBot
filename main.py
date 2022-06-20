import config
import statGetter
from dataScrape import get_and_save
from dataService import get_player_data

player_dict = {}

for url in config.urls.keys():

    # get_and_save(config.urls[url])

    player_dict.update(get_player_data(url, player_dict))


print(statGetter.randomize_attribute(statGetter.remove_default_attributes(player_dict[list(player_dict.keys())[0]])))

