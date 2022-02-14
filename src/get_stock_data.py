from utils import get_hist_data, get_index_positions
import csv 
import os

parent_dir = os.path.dirname(os.getcwd())
data_dir = data_dir = os.path.join(os.path.join(parent_dir,"data"), "b3symbols.csv")

with open(data_dir, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

symbols = [''.join(x) for x in data]
index_position = get_index_positions(symbols, ' Código ')
#get only stocks, excluding FII and BDRS 
symbols = symbols[index_position[0]+1:index_position[1]]

symbols = [symbols[k].strip() +'.SA' for k in range(len(symbols))]
indices = ['^BVSP', '^IEE', 'IMAT.SA']

hist_data = get_hist_data(symbols+indices, '1d')

adj_close = hist_data['Adj Close']
close_price = hist_data['Close']
high_price = hist_data['High']
open_price = hist_data['Open']
low_price = hist_data['Low']
volume = hist_data['Volume']

adj_close.to_csv(os.path.join(os.path.join(parent_dir,"data"), "df_adj_close.csv"))
close_price.to_csv(os.path.join(os.path.join(parent_dir,"data"), "df_close.csv"))
open_price.to_csv(os.path.join(os.path.join(parent_dir,"data"), "df_open.csv"))
high_price.to_csv(os.path.join(os.path.join(parent_dir,"data"), "df_high.csv"))
low_price.to_csv(os.path.join(os.path.join(parent_dir,"data"), "df_low.csv"))
volume.to_csv(os.path.join(os.path.join(parent_dir,"data"), "volume.csv"))