from dataScrape import get_web_content, get_table, save_table_to_csv
from dataService import get_player_data, get_player_data
from config import urls

get_web_content()

player_dict = get_player_data({})

