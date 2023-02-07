# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
import pandas as pd

ticker = 'MCD'
here = os.path.abspath(__file__)
input_dir = os.path.abspath(os.path.join(here, os.pardir))
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:
    with open(ticker_file) as f:
        MCDdf = pd.read_csv(f)  # Turn into pandas dataframe.
    print('opened file for ticker: ', ticker)
    f.close()


except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)

ticker2 = 'SPY'
ticker2_file = os.path.join(input_dir, ticker2 + '.csv')

try:
    with open(ticker2_file) as f2:
        SPYdf = pd.read_csv(f2)  # Turn into pandas dataframe.
    print('opened file for ticker: ', ticker2)
    f.close()


except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker2)
