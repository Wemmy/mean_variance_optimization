import yfinance as yf
from config import symbols
from visulize import cumulative_return_vis

def get_data(symbols: list, start_date: str, end_date:str ):
    return yf.download(symbols, start= start_date, end=end_date)


if __name__ == '__main__':
    d = get_data(symbols, start_date = '2020-01-01',end_date= '2023-11-01')
    cumulative_return_vis(d)
   

