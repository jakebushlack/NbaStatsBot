import config
from dataScrape import get_web_content, get_table, save_table_to_csv
from dataService import get_player_data, get_player_data

player_dict = {}

for url in config.urls.keys():

    get_web_content(config.urls[url])

    player_dict.update(get_player_data(url, player_dict))
