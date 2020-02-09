import urllib.parse
import urllib.request

####使用urllib库 post请求，

def main():
    # 要访问的url地址
    url = 'https://fanyi.baidu.com/sug'

    #表单数据
    form_data = {
        'kw':'post'
    }
    #数据进行编码
    #encode将字符串转化成字节
    form_data = urllib.parse.urlencode(form_data).encode()

    # 模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    }
    # 构建请求对象
    request = urllib.request.Request(url=url, headers=headers)

    # 发送请求
    response = urllib.request.urlopen(request,data=form_data)

    print(response.read())



if __name__ == '__main__':
    main()