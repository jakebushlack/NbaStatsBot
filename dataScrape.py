import datetime
import types

import requests
import csv
from bs4 import BeautifulSoup
from config import urls


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
    file_name =  "stat_files/" +  str(_table["id"])  # + '_' + str(datetime.date.today()))
    if len(_table) > 0:
        header = _table.find("thead").find("tr").find_all("th")
        output_header = ''
        for head in header:
            if head.text != 'Rk':
                output_header += str(head['data-stat'] + ',')

        output_header = output_header[0:-1]
        body = _table.find("tbody")
        rows = body.find_all("tr", "full_table")
        print(len(rows))
        with open(file_name, 'w', encoding='UTF-8') as csv_file:
            csv_file.write(str(output_header) + '\n')
            for row in rows:
                row_contents = ''
                columns = row.find_all("td")
                for col in columns:
                    row_contents += (str(col.text) + ',')
                row_contents = row_contents[0:-1]
                print(row_contents)
                csv_file.write(str(row_contents) + '\n')


response = get_web_content(urls['per_game'])
table = get_table(response)
save_table_to_csv(table)
