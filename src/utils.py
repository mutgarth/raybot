from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas_datareader.data as pdr
import yfinance as yf


def get_webdriver_content(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options = chrome_options, service=Service(ChromeDriverManager().install()))
    driver.get(url)
    content = driver.page_source
    return content

def request_web_content(url):
    page = requests.get(url)
    return page.text, page.status_code

def get_hist_data(symbols, interval):
    yf.pdr_override()
    stocks = pdr.get_data_yahoo(symbols, period='max', interval=interval, group_by = 'column')
    return stocks

def get_index_positions(list_of_elems, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = list_of_elems.index(element, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list