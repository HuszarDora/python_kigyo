import pandas as pd
import numpy as np
import os


def read_etf_file(etf):
    filename = os.path.join('input', etf + '.csv')
    df = pd.read_csv(filename, index_col=0)
    df.index = pd.to_datetime(df.index)
    return df


def get_etf_returns(etf_name,
    return_type='log', fieldname='Adj Close'):

    df = read_etf_file(etf_name)
    df = df[[fieldname]]

    df['shifted'] = df.shift(1)
    if return_type=='log':
        df['return'] = np.log(df[fieldname]/df['shifted'])
    if return_type=='simple':
        df['return'] = df[fieldname]/df['shifted']-1

    # restrict df to result col
    df = df[['return']]
    # rename column
    df.columns = [etf_name]
    # df = df.rename(by=col, {'return': etf_name})
    return df


def get_total_return(etf, return_type='log'):
    return get_etf_returns(etf, return_type, 'Adj Close')


def get_dividend_return(etf, return_type='log'):
    # 1 calc total simple return from Adj Close and Close
    df_ret_from_adj = get_etf_returns(etf, 'simple', 'Adj Close')
    df_ret_from_close = get_etf_returns(etf, 'simple', 'Close')
    # 2 simple div = ret Adj Close simple - ret Close simple
    df_div = df_ret_from_adj - df_ret_from_close
    # 3 convert to log if log
    if return_type=='log':
        df_div = np.log(df_div + 1)
    return df_div


def get_price_return(etf, return_type='log'):
    df_total = get_total_return(etf, 'simple')
    df_div = get_dividend_return(etf, 'simple')
    df_price = df_total - df_div
    if return_type == 'log':
        df_price = np.log(df_price + 1)
    return df_price


def get_portfolio_return(d_weights):
    l_df = []
    for etf, value in d_weights.items():
        df_temp = get_total_return(etf, return_type='simple')
        l_df.append(df_temp)
    df_joined = pd.concat(l_df, axis=1)
    df_joined.sort_index(inplace=True)
    df_joined.dropna(inplace=True)
    df_weighted_returns = df_joined * pd.Series(d_weights)
    s_portfolio_return = df_weighted_returns.sum(axis=1)
    return pd.DataFrame(s_portfolio_return, columns=['pf'])






def osszead(a, b):
    return a+b


def get_portfolio_return_btw_dates(d_weights, from_date=None,to_date=None):
    df = get_portfolio_return(d_weights)
    fromdate = pd.to_datetime(from_date)
    todate = pd.to_datetime(to_date)
    filtered_df = df.loc[fromdate:todate]
    return filtered_df


d_weights = {'IEI': 0.6, 'VOO': 0.4}
print(get_portfolio_return_btw_dates(d_weights, '2020-03-01', '2020-04-15'))


def subtract_trading_date(actual_date, x):
    date = pd.to_datetime(actual_date)
    date_range = pd.bdate_range(end=date, periods=x+1)
    result = date_range[0]
    result_str = result.strftime('%Y-%m-%d')
    return result_str



print(subtract_trading_date('2023-03-28',2))




def calc_historical_var(pf_value, d_weights, l_conf_levels, last_day_of_interval, window_in_days):
    l_quantiles = [1 - x for x in l_conf_levels]
    df_pf = get_portfolio_return(d_weights)
    df_result = df_pf.quantile(l_quantiles)
    df_result.index = l_conf_levels
    return df_result



