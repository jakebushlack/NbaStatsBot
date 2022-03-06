import types

import requests
import csv
from bs4 import BeautifulSoup


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

