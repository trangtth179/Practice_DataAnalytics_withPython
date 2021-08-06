import math
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


def sigmoid(x):
    return 1/(1+ math.exp(-x))

def adf_test(x):
    indices = ['ADF test: ', 'p value', '# of Lags' , '# of Observations']
    test = adfuller(x, autolag='AIC')
    res = pd.Series(test[:4], index=indices)
    for key, value in test[4].items():
        res[f'Critical value({key})'] = value
    return res

def kpss_test(x):
    indices = ['KPSS test: ', 'p value', '# of Lags']
    test = kpss(x)
    res = pd.Series(test[:3], index=indices)
    for key, value in test[3].items():
        res[f'Critical value({key})'] = value
    return res


