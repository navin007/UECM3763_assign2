# -*- coding: utf-8 -*-
from pandas.io.data import DataReader as DR
import pandas as pd
from datetime import datetime as dt
import pylab as p
import numpy as np
import matplotlib.pyplot as plt


start = dt(2012,1,1)
end=dt(2015,1,1)
kenchana = DR("5218.KL",'yahoo',start,end)
klse= DR("^KLSE",'yahoo',start,end)


def moving_avg (values, days):
    weight =np.repeat(1.0, days)/days
    sma=np.convolve(values, weight,'valid')
    return sma

closevalue = kenchana['Close'].values #take only the closing value
ma= moving_avg(closevalue, 5)

number= len(ma)
t= p.linspace(0,number,number);
p.title('5day moving average graph for 5218.KL Sapura Kenchana')
p.xlabel('number of days')
p.ylabel('average of stock price (RM)')
p.plot(t,ma)
p.show()


x = ['5218.KL', '^KLSE']
kenchana_klse_closevalue = DR(x, 'yahoo', start, end)['Close']
correlation_kenchana_klci= kenchana_klse_closevalue.corr()
print('the correlation of  5218.Kl Sapura Kenchana with FTSEKLCI is \n ', correlation_kenchana_klci)
