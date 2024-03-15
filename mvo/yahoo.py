import yfinance as yf
from config import symbols
from visulize import cumulative_return_vis
import seaborn as sns
from pyfopt import expected_returns, risk_models
from pyfopt.efficient_frontier import EfficientFrontier
import numpy as np

def get_data(symbols: list, start_date: str, end_date:str ):
    return yf.download(symbols, start= start_date, end=end_date)


if __name__ == '__main__':
    d = get_data(symbols, start_date = '2018-01-01',end_date = '2023-01-01')

    # msft = yf.Ticker("MSFT")
    # hist = msft.history(period="1mo", start= '2023-11-24')
    # data type: pd.dataframe multiindex
    
    # visulize cumulative return AND show correlation heatmap
    portfolio_returns = d['Adj Close'].pct_change().dropna()

    # calculate cumulative return
    port_comps_rets_cumprod = portfolio_returns.add(1).cumprod().sub(1)*100

    # visulize cumulative return AND show correlation heatmap
    # cumulative_return_vis(port_comps_rets_cumprod)

    # calculate correlation
    port_corr = port_comps_rets_cumprod.corr()
    # sns.heatmap(port_corr)

    # # Compare with Benchmark S&p500
    # sp_index = get_data('^GSPC', start_date = '2020-01-01',end_date= '2023-11-01')

    # optimization
    train = portfolio_returns[:'2021-05-30']
    test = portfolio_returns['2021-05-31':]

    # calculate ema expected return and covrance ()
    mu = expected_returns.ema_historical_return(train, returns_data = True, span = 500)
    sigma = risk_models.exp_cov(train, returns_data = True, span 180)

    # calculated exp
    ret_ef = np.arrange(0, max(mu), 0.01)
    vol_ef = []
    for i in np.arrange(0, max(mu), 0.01):
        ef = EfficientFrontier(mu, sigma)
        ef.efficient_return(i)
        vol_ef.append(ef.portolio_performance()[1])
    
    ef = EfficientFrontier(mu, sigma)
    ef.min_volatility()
    min_vol_ret = ef.protfolio_performance()[0]
    min_vol_vol = ef.protfolio_performance()[1]

    ef = EfficientFrontier(mu, sigma)
    ef.max_sharp(risk_free_rate = 0.05)
    min_vol_ret = ef.protfolio_performance()[0]
    min_vol_vol = ef.protfolio_performance()[1]

    sns.set()

    fig, ax = plt.subplots(figsize = [15,10])

    sns.lineplot(x = vol_ef, y = ret_ef,
                label = "Efficient Frontier",
                ax = ax)

    sns.scatterplot(x = [min_vol_vol], y = [min_vol_ret],
                    ax = ax,
                    label = "Minimum Variance Portfolio",
                    color = "purple", s = 100)

    sns.scatterplot(x = [max_sharpe_vol], y = [max_sharpe_ret],
                    ax = ax,
                    label = "Maximum Sharpe Portfolio",
                    color = "green", s = 100)

    sns.lineplot(x = [0, max_sharpe_vol, 1], y = [0.009, max_sharpe_ret, 3.096],
                label = "Capital Market Line",
                ax = ax,
                color = "r")

    ax.set(xlim = [0, 0.4])
    ax.set(ylim = [0, 1])
    ax.set_xlabel("Volatility")
    ax.set_ylabel("Mean Return")
    plt.legend(fontsize='large')
    plt.title("Efficient Frontier", fontsize = '20')
   

