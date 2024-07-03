import tad
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings("ignore")

def dparserfunc(date):
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

data = pd.read_csv("resources/data/test_data_1.csv", index_col='timestamp',
                       parse_dates=True,
                       date_parser=dparserfunc)
values = data['count'].values
data = data.squeeze()
idxs = data.index.values

ans = tad.anomaly_detect_ts(data, direction='both', 
                  alpha=0.05, plot=False, longterm=True)

ans = ans['anoms']
ans_ts = ans.index.values
idxs = [[idx for idx, val in enumerate(idxs) if val == i] for i in ans_ts]

plt.plot(values, color = "blue")
for idx in idxs:
    plt.scatter(idx, values[idx], color = "red")
plt.savefig("SAMPLE.png")
plt.close()