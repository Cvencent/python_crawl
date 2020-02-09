import json
import requests
import jsonpath

def main():

    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
    # 模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    }
    # 创建请求信息
    response = requests.get(url, headers = headers)

    # 将json字符串转化成对象
    jsonobj = json.loads(response.text)

    # 匹配相应的信息
    titles = jsonpath.jsonpath(jsonobj,'$.subjects..title') # $..title是一样的

    srcs = jsonpath.jsonpath(jsonobj,'$..url')

    # 递归返回
    for title,src in zip(titles,srcs):
        yield {
            'title':title,
            'src':src,
        }

if __name__ == '__main__':
    for item in main():
        print(item)