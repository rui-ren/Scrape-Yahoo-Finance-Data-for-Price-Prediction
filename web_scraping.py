# web scrabe the finance data

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

plt.rcParams['figure.figsize'] = (20,10)
style.use('seaborn')

import requests
import json
import numpy as np
from urllib import parse
import time
from datetime import datetime
from matplotlib import pyplot
import random

def get_data(url, key):
    
    if key:
        url = url.format(key)
    url = url.format(key)
    feedback = requests.get(url)
    res = json.loads(feedback.text)

    df = res['series'][0]['data']

    Year = [i[0][:4] + '-' + i[0][4:] for i in df]
    ind = [datetime.strptime(i, '%Y-%M') for i in Year]
    sales_value = [i[1] for i in df]    
    
    return sales_value


def test_code():

    sales_val_url = "http://api.eia.gov/series/?api_key={}&series_id=PET.C720010001.M"
    sales_val_key = "785919979cec4205e9f2210244b0c78b"
    sales_data = get_data(sales_val_url, sales_val_key)
    
    # Figure for sales
    plt.plot(range(len(sales_data)), sales_data, 'r')
    plt.show()
    # Figure for price
    plt.figure()
    price_val_url = " http://api.eia.gov/series/?api_key={}&series_id=PET.EMD_EPD2DXL0_PTE_R10_DPG.M"
    price_val_key = "785919979cec4205e9f2210244b0c78b"
    price_data = get_data(price_val_url, price_val_key)
    plt.plot(range(len(price_data)), price_data, 'blue')
    
    plt.show()


if __name__ == "__main__":
    
    random.seed(0)
    test_code()