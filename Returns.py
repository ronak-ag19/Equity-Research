import sys
import pandas as pd
import datetime as dt

stock_symbol=input("enter the Stock Symbol: ")

start_date=str(int(dt.datetime(2018,10,1).timestamp())+19800) 
end_date=str(int(dt.datetime(2019,9,30).timestamp())+19800)

freq=['1d','1wk','1mo']    
event="history"

url_list=[]
for i in freq:
    url="https://query1.finance.yahoo.com/v7/finance/download/"\
     +stock_symbol+".NS?period1="+start_date+"&period2="+end_date+"&interval="\
     +i+"&events="+event+"&includeAdjustedClose=true"
    url_list.append(url)
    
factor="Close"                   
new_column=["Daily Returns (%)","Weekly Returns (%)","Monthly Returns (%)"]
table=[daily_data,weekly_data,monthly_data]
    
daily_data=pd.read_csv(url_list[0])
daily_data[new_column[0]]=(table[0][factor]/table[0][factor].shift(1)-1)*100

weekly_data=pd.read_csv(url_list[1])
weekly_data[new_column[1]]=(table[1][factor]/table[1][factor].shift(1)-1)*100

monthly_data=pd.read_csv(url_list[2])
monthly_data[new_column[2]]=(table[2][factor]/table[2][factor].shift(1)-1)*100
    
data=pd.concat([daily_data,weekly_data,monthly_data],axis=1)
data=round(data[new_column].describe().iloc[[1,2,3,7]],2)

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

data.style.applymap(color_negative_red).highlight_max(color = 'lightgreen', axis = 1)
