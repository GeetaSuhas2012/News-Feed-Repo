import requests
import pandas as pd
from datetime import datetime, timedelta, timezone
# datetime object containing current date and time
from dateutil.parser import parse

now = datetime.now()
#print(type(now))
dt = now.strftime("%d/%m/%Y %H:%M:%S")
dt = parse(dt, fuzzy=True)
print(now)
list_csv=['NBC.csv','TOI.csv']
df = pd.read_csv("NBC.csv")
#print(df.columns)
date = df['Pub_Date'].tolist()
flag = []
print(date)
for i in range(len(date)):
    date[i]= parse(date[i], fuzzy=True)
    print(type(dt))
    print(type(date[i]))
    # dt = dt.time()
    # date[i] = date[i].time()
    if dt > date[i]:
      flag[i].append(1)
    else:
      flag[i].append(2)
    #
    # print(date[i])

    #date[i]=date[i].strftime("%d/%m/%Y %H:%M:%S")
#print(date)
#print(df['Pub_Date'])