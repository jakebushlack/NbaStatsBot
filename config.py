import datetime
import logging

logging.basicConfig(filename=f'logs/log_output_{datetime.date.today()}.log', filemode='w',
                    format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    encoding='utf-8', level=logging.DEBUG)

urls = {
    'per_game': 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html',
    'totals': 'https://www.basketball-reference.com/leagues/NBA_2022_totals.html',
    'per_minute': 'https://www.basketball-reference.com/leagues/NBA_2022_per_minute.html',
    'per_poss': 'https://www.basketball-reference.com/leagues/NBA_2022_per_poss.html'
}

test_content = {
    'test_html': 'test_html.html',
    'test_csv': ['per_game', 'totals']
}
