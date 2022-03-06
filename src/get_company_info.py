from re import S
import yfinance as yf
import sys
sys.path.append('../src/')
import os
import pandas as pd
import csv
from utils import get_index_positions
from datetime import datetime

parent_dir = os.path.dirname(os.getcwd())
data_dir = os.path.join(os.path.join(parent_dir,"data"), "b3symbols.csv")

with open(data_dir, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

symbols = [''.join(x) for x in data]
index_position = get_index_positions(symbols, ' Código ')
symbols = symbols[index_position[0]+1:index_position[1]]
symbols = [symbols[k].strip() +'.SA' for k in range(len(symbols))]
symbols = symbols

lista = []
nlista = []

i = 0

for symbol in symbols:
    try:
        data = yf.Ticker(symbol)
        sector = data.info.get('sector')
        industry = data.info.get('industry')
        ts = data.info.get('lastSplitDate')
        if ts is None:
            split_year = 0
            split_factor = 0
        else:
            split_year = datetime.utcfromtimestamp(int(ts)).strftime('%Y')
            split_factor = data.splits[len(data.splits)-1]
        num_shares = data.info.get('sharesOutstanding')
        lista.append([symbol,sector,industry,split_year,split_factor,num_shares])
        i+=1
        print(symbol + ' has Finished --- ' + str(i) + ' of ' + str(len(symbols)))
    except:
        i+=1
        print(symbol + ' has Failed')
        nlista.append(symbol)
        pass

columns = ['Stock', 'Sector', 'Industry','Split Year','Split Factor','Num Shares']

df = pd.DataFrame(lista, columns=columns)

df.to_csv(os.path.join(os.path.join(parent_dir,"data"), "companyInfos.csv"), index=False)

print(nlista)