from bs4 import BeautifulSoup
import requests
import os

URL = "http://www.ngchina.com.cn/animals/"
html = requests.get(url=URL).text
soup = BeautifulSoup(html, features="lxml")
img_url = soup.find_all('ul', {'class': 'img_list'})
os.makedirs('./img/', exist_ok=True)

for ul in img_url:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url=url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print("Saved %s" % image_name)
