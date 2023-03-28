import unittest
import utils as u
import pandas as pd
import numpy as np
import os

# from utils import read_etf_file, get_etf_returns, get_total_return, get_dividend_return, get_price_return, \
#     get_portfolio_return, calc_historical_var, osszead, get_portfolio_return_btw_dates


class MyTest(unittest.TestCase):

    def test_get_portfolio_return_btw_dates(self):
        d_weights = {'IEI': 0.6, 'VOO': 0.4}
        df = u.get_portfolio_return_btw_dates(d_weights, '2020-03-01', '2020-04-15')
        self.assertEqual(len(df.index), 32)
        self.assertAlmostEqual(32.1111, 32.1112, 3)

    def test_subtract_trading_date(self):
        df = u.subtract_trading_date('2023-03-28',2)
        self.assertEqual(df, '2023-03-24')

    # def test_osszead(self):
    #     c = osszead(2, 3)
    #     self.assertEqual(c, 5)
    #
    #
    #
    #
    # def test_read_etf_file(self):
    #     df = read_etf_file('SPY')
    #     self.assertIsInstance(df, pd.DataFrame)
    #
    # def test_get_etf_returns(self):
    #     df = get_etf_returns('SPY')
    #     self.assertIsInstance(df, pd.DataFrame)
    #     self.assertEqual(df.columns[0], 'SPY')
    #
    # def test_get_total_return(self):
    #     df = get_total_return('SPY')
    #     self.assertIsInstance(df, pd.DataFrame)
    #     self.assertEqual(df.columns[0], 'SPY')
    #
    # def test_get_dividend_return(self):
    #     df = get_dividend_return('SPY')
    #     self.assertIsInstance(df, pd.DataFrame)
    #     self.assertEqual(df.columns[0], 'SPY')
    #
    # def test_get_price_return(self):
    #     df = get_price_return('SPY')
    #     self.assertIsInstance(df, pd.DataFrame)
    #     self.assertEqual(df.columns[0], 'SPY')
    #
    # def test_get_portfolio_return(self):
    #     d_weights = {'SPY': 0.5, 'QQQ': 0.5}
    #     df = get_portfolio_return(d_weights)
    #     self.assertIsInstance(df, pd.DataFrame)
    #     self.assertEqual(df.columns[0], 'pf')
    #
    # def test_calc_historical_var(self):
    #     d_weights = {'SPY': 0.5, 'QQQ': 0.5}
    #     l_conf_levels = [0.95, 0.99]
    #     df = calc_historical_var(d_weights, l_conf_levels)
    #     self.assertIsInstance(df, pd.Series)
    #     self.assertEqual(df.index.tolist(), l_conf_levels)
