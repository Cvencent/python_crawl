import urllib.request
import urllib.parse

####使用urllib库 普通get请求，


def main():
    #要访问的url地址
    url = 'https://www.baidu.com/'

    #get参数
    Query_String = {
        'wd' :'urllib',
        'ie' :'utf-8'
    }
    #将参数转化成url格式
    Query_String = urllib.parse.urlencode(Query_String)

    #拼接url
    url = url + '?' + Query_String

    #模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    }
    #构建请求对象
    request = urllib.request.Request(url = url ,headers = headers)

    #发送请求
    response = urllib.request.urlopen(request)

    print(response.read().decode())




if __name__ == '__main__':
    main()