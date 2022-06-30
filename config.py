import os

urls = {
    'per_game': 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html',
    'totals': 'https://www.basketball-reference.com/leagues/NBA_2022_totals.html',
    'per_minute': 'https://www.basketball-reference.com/leagues/NBA_2022_per_minute.html',
    'per_poss': 'https://www.basketball-reference.com/leagues/NBA_2022_per_poss.html'
}

test_content = {
    'test_html': 'test_html.html',
    'test_table': 'stat_files/test_table_stats.csv'
}

stat_files_path = f'{os.getcwd()}/stat_files'
log_files_path = f'{os.getcwd()}/logs'

# logging configuration in setup.py
