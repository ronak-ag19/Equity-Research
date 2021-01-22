import sys
import pandas as pd
import datetime as dt

stock_symbol=input("enter the Stock Symbol: ")

start_date=str(int(dt.datetime(2019,11,1).timestamp())+19800) 
end_date=str(int(dt.datetime(2020,12,29).timestamp())+19800)

freq=['1d','1wk','1mo']    
event="history"

url_list=[]
for i in freq:
    url="https://query1.finance.yahoo.com/v7/finance/download/"\
     +stock_symbol+".NS?period1="+start_date+"&period2="+end_date+"&interval="\
     +i+"&events="+event+"&includeAdjustedClose=true"
    url_list.append(url)
    
factor="Close"                   
new_column=["Daily Freq","Weekly Freq","Monthly Freq"]
#table=[daily_data,weekly_data,monthly_data]
    
daily_data=pd.read_csv(url_list[0])
daily_data[new_column[0]]=(daily_data[factor]/daily_data[factor].shift(1)-1)*100

weekly_data=pd.read_csv(url_list[1])
weekly_data[new_column[1]]=(weekly_data[factor]/weekly_data[factor].shift(1)-1)*100

monthly_data=pd.read_csv(url_list[2])
monthly_data[new_column[2]]=(monthly_data[factor]/monthly_data[factor].shift(1)-1)*100
    
data=pd.concat([daily_data,weekly_data,monthly_data],axis=1)
data=round(data[new_column].describe().iloc[[1,2,3,7]],2)
data.loc['Return/Risk']=data.loc['mean']/data.loc['std']
data = data.rename(index={'mean': 'Mean Return (%)',
                         'std':'Mean Risk(%)',
                         'min':'Min Return(%)',
                         'max':'Max Return(%)'})
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

data.style.applymap(color_negative_red).highlight_max(color = 'lightgreen', axis = 1)
