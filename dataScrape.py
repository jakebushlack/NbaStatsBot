import logging
import requests
from bs4 import BeautifulSoup


def get_web_content(_url):  # should just do the web request and return the request
    logging.debug(f'Requesting web content for {_url}')
    r = requests.get(_url)
    logging.debug(f'Content for {_url} retrieved')

    return r


def content_to_html(_web_content):
    return BeautifulSoup(_web_content, 'html.parser')


def get_table_from_html(_web_content):  # should take the request and find the table Tag
    soup = content_to_html(_web_content)
    return soup.find("table", {"class": "stats_table"})


def save_table_to_csv(_table):  # should take the table Tag and save its contents to a .csv
    file_name = f'stat_files/{str(_table["id"])}.csv'

    logging.debug(f'Beginning parse table to csv')

    if len(_table) > 0:
        header = _table.find("thead").find("tr").find_all("th")
        output_header = ''

        logging.debug(f'Building stat header')

        for head in header:
            if head.text != 'Rk':
                output_header += str(head['data-stat'] + ',')

        output_header = output_header[0:-1]
        body = _table.find("tbody")

        rows = body.find_all("tr", "full_table")

        with open(file_name, 'w', encoding='UTF-8') as csv_file:
            csv_file.write(str(output_header) + '\n')

            logging.debug(f'Building player rows')

            for row in rows:
                row_contents = ''
                columns = row.find_all("td")

                for col in columns:
                    row_contents += (str(col.text) + ',')

                row_contents = row_contents[0:-1]
                csv_file.write(str(row_contents) + '\n')

        logging.debug(f'Data table saved to {file_name}')


def get_and_save(_url):
    content = get_web_content(_url).content
    table = get_table_from_html(content)
    save_table_to_csv(table)
