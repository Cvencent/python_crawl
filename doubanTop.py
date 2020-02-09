import json
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url,**headers):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return 'Exception'

def parse_one_page(html):
    pattern = re.compile('<div class="hd".*?href="(.*?)".*?"title">(.*?)</span>.*?"bd">.*?<p class="">(.*?)</p>.*?"star">.*?"v:average">(.*?)</span>.*?inq">(.*?)</span>', re.S)
    items =  re.findall(pattern, html)
    for item in items:
        yield {
            'url':item[0],
            'name':item[1],
            'actor':re.sub('&nbsp;|...<br>\\n', '', item[2].strip()),
            'motor':item[3]
        }

def write_to_file(content):
    with open('doubanTop250.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n' )


def main(num):
    url = 'https://movie.douban.com/top250?start='+str(num)+'&filter='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    html = get_one_page(url,**headers)
    for item in parse_one_page(html):
        print (item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(0,225,25):
        main(i)