from bs4 import BeautifulSoup
import numpy as np
import os

from utils import get_web_content

content = get_web_content("https://valorinveste.globo.com/cotacoes/")
soup = BeautifulSoup(content, "lxml")
symbols=[]

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
