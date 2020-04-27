import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


amj = web.get_data_yahoo("AMJLAND.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")

amj_monthly_returns = amj['Close'].resample('M').ffill().pct_change()
                #resampling all dates on basis of month and forward filling the data
                #even if the last day of the month is a holiday, the previous day is taken and filled in that day
amj_monthly_returns = amj_monthly_returns *100


print("Monthly Returns")
print("Maximum:"+ str(round(amj_monthly_returns.max(axis=0),3)))    
print("Minimum:"+str(round(amj_monthly_returns.min(axis=0),3)))  
print("Mean:"+str(round(amj_monthly_returns.mean(),3)))  
print("Sample Standard Deviation:"+str(round(amj_monthly_returns.std(axis=0),3)))

amj_monthly_returns.to_csv (r'D:\000Finance\FOFA ASSIGNMENT 2\85_Shubh_2018A2PS0832H_DELTACORP\4 monthly returns (risk unadjusted) AMJLAND.csv', header=True)