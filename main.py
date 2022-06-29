import setup
import config
import statGetter
import twitterService
from dataScrape import get_web_content, get_html_from_bytes
from dataService import get_player_data
from htmlTableReader import get_table_from_html_and_save_as_csv


setup.ensure_logs_dir_exists(config.log_files_path)
setup.configure_logging()
setup.ensure_stat_files_dir_exists(config.stat_files_path)


player_dict = {}
random_stats = []
players_of_interest = []

for url in config.urls.keys():
    html = get_html_from_bytes(get_web_content(config.urls[url]).content)
    get_table_from_html_and_save_as_csv(html)

    player_dict.update(get_player_data(url, player_dict))


default_player = player_dict[list(player_dict.keys())[0]]

while len(players_of_interest) < 1:
    random_stats = default_player.get_three_random_attributes()
    print(random_stats)
    players_of_interest = statGetter.find_top_tens(random_stats, player_dict)

twitterService.generate_tweet(player_dict, players_of_interest, random_stats)
