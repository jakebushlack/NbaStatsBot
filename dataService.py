import types

from StatCategories import StatCategories
from Player import Player

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


# content = get_web_content(urls['per_game'])
# table = get_table(content)
# stat_categories = get_stat_categories(table)
#
# # get_player_data(table, stat_categories)
# # print(table["id"])
# save_table_to_csv(table)
