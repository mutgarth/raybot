from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import numpy as np
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://valorinveste.globo.com/cotacoes/")

symbols=[]

content = driver.page_source
soup = BeautifulSoup(content, "lxml")

rows = soup.findAll('tr')

for tr in rows:
    try:
        symbols.append(tr.select('td')[1].text)
    except Exception:
        pass


symbols = [symbols[k].strip() +'.SA' for k in range(len(symbols))]

parent_dir = os.path.dirname(os.getcwd())
data_dir = os.path.join(os.path.join(parent_dir,"data"), "b3symbols.csv")

np.savetxt(data_dir, symbols, delimiter=", ", fmt='% s')
