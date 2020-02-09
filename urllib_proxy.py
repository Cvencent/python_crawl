import urllib.parse
import urllib.request

### 高级用法 代理

def main():
    # 要访问的url地址
    url = 'https://www.baidu.com/s'

    # get参数
    query_string = {
        'wd': 'ip',
        'ie': 'utf-8'
    }
    # 将参数转化成url格式
    query_string = urllib.parse.urlencode(query_string)

    # 拼接url
    url = url + '?' + query_string

    print(url)

    # 模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    }

    # 创建一个代理handler
    handler = urllib.request.ProxyHandler({'http':'123.169.114.128:9999'})

    # 创建opener
    opener = urllib.request.build_opener(handler)

    # 构建请求对象
    request = urllib.request.Request(url=url, headers=headers)

    # 发送请求
    response = opener.open(request)
    # 写入文件
    with open('ip.html','wb') as fp:
        fp.write(response.read())



if __name__ == '__main__':
    main()
