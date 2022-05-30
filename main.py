import config
from dataScrape import get_and_save
from dataService import get_player_data

player_dict = {}

for url in config.urls.keys():

    get_and_save(config.urls[url])

    player_dict.update(get_player_data(url, player_dict))
