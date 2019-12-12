import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
plt.rcParams['figure.figsize']=(20,10)
import requests
import json
import numpy as np
from urllib import parse
from datetime import datetime
import time
from matplotlib import pyplot

urlformat = "http://api.eia.gov/series/?api_key={}&series_id=PET.C720010001.M"
Key = "785919979cec4205e9f2210244b0c78b"
url = urlformat.format(Key)
feedback = requests.get(url)
res = json.loads(feedback.text)

df = res['series'][0]['data']

Year = [i[0][:4] + '-' + i[0][4:] for i in df]
ind = [datetime.strptime(i, "%Y-%m") for i in Year]
value = [i[1] for i in df]

## we can see has nan value
plt.plot(ind, value)
plt.xlabel('Year')
plt.ylabel('Value')
ax = plt.gca()
ax.xaxis.grid(True, which='Major', linestyle='--')
ax.yaxis.grid(True, which='Major', linestyle='--')

# switch to pandas
df1 = pd.DataFrame(index = ind)
df1['data'] = np.array(value)
df1 = df1[::-1]
df1.plot(legend=None)
plt.title('PADD 1 No.2 Diesel All Sales/Deliveries by Prime Supplier from 2007 to 2019')
plt.xlabel('Time')
plt.ylabel('PADD 1 No.2 Diesel All Sales/Deliveries by Prime Supplier(Thousand Gallons per Day)')

# DJI
df_DJI=web.get_data_yahoo('^DJI','01/01/2007','09/02/2019',interval='m')
data2=pd.DataFrame(data=df_DJI['Close'])

df1.corrwith(data2, axis = 1) 