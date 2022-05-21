import requests
from bs4 import BeautifulSoup
import config


def get_web_content():
    for _url in config.urls.values():
        r = requests.get(_url)
        table = get_table(r.content)
        save_table_to_csv(table)


def get_table(_web_content):
    table = ''
    if len(_web_content) > 0:
        soup = BeautifulSoup(_web_content, 'html.parser')
        table = soup.find("table", {"class": "stats_table"})

    return table


def save_table_to_csv(_table):
    file_name = (f'stat_files/{str(_table["id"])}.csv')

    if len(_table) > 0:
        header = _table.find("thead").find("tr").find_all("th")
        output_header = ''

        for head in header:
            if head.text != 'Rk':
                output_header += str(head['data-stat'] + ',')

        output_header = output_header[0:-1]
        body = _table.find("tbody")
        rows = body.find_all("tr", "full_table")

        with open(file_name, 'w', encoding='UTF-8') as csv_file:
            csv_file.write(str(output_header) + '\n')

            for row in rows:
                row_contents = ''
                columns = row.find_all("td")

                for col in columns:
                    row_contents += (str(col.text) + ',')

                row_contents = row_contents[0:-1]
                csv_file.write(str(row_contents) + '\n')

