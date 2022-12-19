import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


def parse_xml(url):
    # Initializing soup variable
    xml_data = requests.get(url).content
    soup = BeautifulSoup(xml_data, 'xml')

    # Creating column for table
    df = pd.DataFrame(columns=['guid', 'title', 'pubDate', 'description'])

    # Iterating through item tag and extracting elements
    all_items = soup.find_all('item')
    items_length = len(all_items)
    Title = []
    Link = []
    Pub_Date = []
    Description = []

    for index, item in enumerate(all_items):
        guid = item.find('guid').text
        Link.append(guid)
        title = item.find('title').text
        Title.append(title)
        pub_date = item.find('pubDate').text
        Pub_Date.append(pub_date)
        description = item.find('description').text
        Description.append(description)

        # Adding extracted elements to rows in table
    df = pd.DataFrame(list(zip(Link, Title, Pub_Date, Description)), columns =['Link', 'Title', 'Pub_Date', 'Description'])

    return df
newsdf = pd.read_csv("news feed.csv")
#print(newsdf)
#print(newsdf.columns)
url_list = newsdf[' News feed Url'].values.tolist()
new_site = newsdf['News Origin'].values.tolist()
flag = []

print(url_list)
for i in range(len(url_list)):
    df = parse_xml(url_list[i])
    a = new_site[i]
    print(a)
    # date_f = []
    # for j in range(len(df['Pub_Date'])):
    #      date_f.append(df['Pub_Date'[j]].strftime("%d/%m/%Y %H:%M:%S"))
    df.to_csv(f"{a}.csv", index=True, encoding='utf-8')

    flag.append(1)
newsdf[' Active flag'] = flag
print(newsdf[' Active flag'])
print(newsdf)
df.to_csv("news feed active.csv")
