import logging
import requests
from bs4 import BeautifulSoup


def get_web_content(_url):  # should just do the web request and return the request
    logging.debug(f'Requesting web content for {_url}')
    r = requests.get(_url)
    logging.debug(f'Content for {_url} retrieved')

    return r


def get_html_from_bytes(_web_content):
    return BeautifulSoup(_web_content, 'html.parser')
