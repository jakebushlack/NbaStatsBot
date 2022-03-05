import types

import requests
import csv
from bs4 import BeautifulSoup
from StatCategories import StatCategories
from config import urls
from Player import Player


def get_web_content(_url):
    r = requests.get(_url)
    return r


def get_table(_request):
    table = ''
    if _request.status_code == 200:
        soup = BeautifulSoup(_request.content, 'html.parser')
        table = soup.find("table", {"class": "stats_table"})

    return table

def save_table_to_csv(_table):
    file_name = _table["id"]
    if len(_table) > 0:
        header = _table.find("thead").find("tr").select("[aria-label]")
        body = _table.find("tbody")
        rows = body.find_all("tr", "full_table")
        row_contents = ''
        print(len(rows))
        for row in rows:
            name = ''
            last_first = row.find("td", {"data-stat": "player"})
            if len(last_first) > 0:
                name = last_first["csk"]

            columns = row.find_all("td")
            print(name)
            for col in columns:
                content = col.text

def get_stat_categories(_table):
    stat_categories = StatCategories()

    if len(_table) > 0:
        header = _table.find("thead").find("tr").select("[aria-label]")
        for col in header:
            stat_categories.stat_categories_text.append(col.text)
            stat_categories.stat_categories_concise.append(col['data-stat'])
            stat_categories.stat_categories_verbose.append(col['aria-label'])

            print('"' + str(col['data-stat']) + '"' + ": " + '"' + str(col['aria-label']) + '"')

    return stat_categories


def get_player_data(_table):
    players = []
    body = _table.find("tbody")
    rows = body.find_all("tr", "full_table")
    print(len(rows))
    for row in rows:
        columns = row.find_all("td")
        player = Player(columns)
        for col in columns:
            player.adding_new_attr(str(col['data-stat']), str(col.text))
            print('"' + str(col['data-stat']) + '"' + ": " + '"' + str(col.text) + '"')
        players.append(player)

    print(len(players))
    print(players[0].pos)

def get_player_stats(_table, _name):
    body = _table.find("tbody")
    player_row = body.find_all("tr", "full_table")


def join_player_data(_player, _stats):
    return []


content = get_web_content(urls['per_game'])
table = get_table(content)
stat_categories = get_stat_categories(table)

# get_player_data(table, stat_categories)
# print(table["id"])
save_table_to_csv(table)
