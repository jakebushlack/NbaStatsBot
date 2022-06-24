import logging


def get_table_from_html(_html):  # should take the request and find the table Tag
    return _html.find("table", {"class": "stats_table"})


def save_table_to_csv(_table):  # should take the table Tag and save its contents to a .csv
    file_name = f'stat_files/{str(_table["id"])}.csv'

    logging.debug(f'Beginning parse table to csv')

    if len(_table) > 0:
        header_row = get_header_row(_table)
        rows = get_player_rows(_table)

        write_text_to_csv(file_name, header_row, rows)

        logging.debug(f'Data table saved to {file_name}')


def get_header_row(_table):
    header = _table.find("thead").find("tr").find_all("th")
    header_text = ''

    logging.debug(f'Building stat header')

    for head in header:
        if head.text != 'Rk':
            header_text += str(head['data-stat'] + ',')

    return header_text[0:-1]


def get_player_rows(_table):
    body = _table.find("tbody")
    return body.find_all("tr", "full_table")


def get_text_from_row_element(_row):
    row_contents = ''
    columns = _row.find_all("td")

    for col in columns:
        row_contents += (str(col.text) + ',')

    return row_contents[0:-1]


def write_text_to_csv(_file_name, _header_row, _stat_rows):
    with open(_file_name, 'w', encoding='UTF-8') as csv_file:
        csv_file.write(str(_header_row) + '\n')

        logging.debug(f'Building player rows')

        for row in _stat_rows:
            row_stat_text = get_text_from_row_element(row)
            csv_file.write(str(row_stat_text) + '\n')


def get_table_from_html_and_save_as_csv(_html):
    table = get_table_from_html(_html)
    save_table_to_csv(table)
