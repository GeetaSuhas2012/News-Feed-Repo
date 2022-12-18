import csv
import pandas as pd
import psycopg2
import glob
import requests
from bs4 import BeautifulSoup
import xml
print("Enter news url:")
url = input()
# Request
r1 = requests.get(url)
r1.status_code
# We'll save in coverpage the cover page content
coverpage = r1.content
# Soup creation
soup1 = BeautifulSoup(coverpage, feature='html.parser')
# News identification
coverpage_news = soup1.find_all('h2', class_='articulo-titulo')
coverpage_news[4].get_text()
coverpage_news[4]['href']

number_of_articles = 5
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []

for n in np.arange(0, number_of_articles):

    # only news articles (there are also albums and other things)
    if "inenglish" not in coverpage_news[n].find('a')['href']:
        continue

    # Getting the link of the article
    link = coverpage_news[n].find('a')['href']
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='articulo-cuerpo')
    x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

    # df_features
    df_features = pd.DataFrame(
        {'Article Content': news_contents
         })

    # df_show_info
    df_show_info = pd.DataFrame(
        {'Article Title': list_titles,
         'Article Link': list_links})
    df_features

# conn = psycopg2.connect(database="postgres", user='postgres', password='data123', host='localhost', port= '5432')
# cursor = conn.cursor()
# data = pd.read_csv("TOI.csv")
# # data.to_sql(tablename, conn, if_exists='append', index=False)
# print(data.columns)
# # cursor.execute('''create table tb(
# # link_n text,
# # title text,
# # pub_date text,
# # description text);''')
# # # data.drop['Unnamed: 0']
# for i in data.index:
#     a = data['Link'][i]
#     b = data['Title'][i]
#     c = data['Pub_Date'][i]
#     d = data['Description'][i]
#     cursor.execute('''INSERT INTO tb(link_n, title, pub_date, description) values('%s', '%s', '%s', '%s');'''%(a, b, c, d))
#     conn.commit()
#
# # Close the connection
# cursor.close()
# conn.close()
