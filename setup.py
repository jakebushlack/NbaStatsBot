import datetime
import logging
import os


def ensure_logs_dir_exists(logs_path):
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
    configure_logging()


def configure_logging():
    logging.basicConfig(filename=f'logs/log_output_{datetime.date.today()}.log', filemode='w',
                        format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        encoding='utf-8', level=logging.DEBUG)


def ensure_stat_files_dir_exists(stat_files_path):
    logging.info(f'Looking for /stat_files directory')

    if not os.path.exists(stat_files_path):
        logging.info(f'/stat_files directory not found, creating new directory')
        os.makedirs(stat_files_path)