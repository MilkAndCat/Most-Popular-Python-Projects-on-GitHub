import requests
import xlwt
from operator import itemgetter


# make an API call and store the response。

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code: ", r.status_code)

ids = r.json()
article_infors = []

for single_id in ids:
    url = 'https://hacker-news.firebaseio.com/v0/item/'+str(single_id)+'.json'
    submission_r = requests.get(url)
    print("Single Status Code:", submission_r.status_code)
    response_dict = submission_r.json()
    article_infor = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id='+str(single_id),
        'comments': response_dict.get('descendants', 0)
    }
    article_infors.append(article_infor)

article_infors = sorted(article_infors, key=itemgetter('comments'), reverse=True)

file_name = 'HackerNews.json'
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

x = 0
for article_infor in article_infors:
        sheet1.write(x, 0, str(article_infor['title']))
        sheet1.write(x, 1, str(article_infor['link']))
        sheet1.write(x, 2, str(article_infor['comments']))
        x += 1


book.save("Top_Stories_HackerNews.xls")