import urllib.parse
import urllib.request

### 高级用法handler
def main():
    # 要访问的url地址
    url = 'https://www.baidu.com/'

    # 模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    }
    # 创建一个普通的handler
    handler = urllib.request.HTTPHandler()

    # 创建opener
    opener = urllib.request.build_opener(handler)
    # 构建请求对象
    request = urllib.request.Request(url = url,headers = headers)
    # 发送请求
    response = opener.open(url)

    print(response.read().decode())

if __name__ == '__main__':
    main()