import pandas as pd
import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = {'title':[],'date':[],'url':[],'likes':[]}

for j in range(1, 46):
    url = f"https://rategain.com/blog/page/{j}"
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    article = soup.select('article.blog-item.category-blog.with-image')
    title_list = soup.select('article.blog-item.category-blog.with-image .content h6 a')
    date_list = soup.select('article.blog-item.category-blog.with-image .blog-detail .bd-item:first-child span')
    url_list = soup.select('article.blog-item.category-blog.with-image  .wrap .img a')
    likes_list = soup.select('article.blog-item.category-blog.with-image .wrap .content > a.zilla-likes i ~ span')
    for i in range(len(article)):
        for x in title_list[i]:
            data['title'].append(x.string)
        for x in date_list[i]:
            data['date'].append(x.string)
        data['url'].append(url_list[i].get('data-bg'))
        data['likes'].append(likes_list[i].contents[0])
ff = pd.DataFrame.from_dict(data)
ff.to_csv("nik.csv",index=False)
