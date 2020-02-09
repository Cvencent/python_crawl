import requests
from lxml import etree


def main():
    # 用来储存结果的列表
    items = []
    # 访问地址
    url = 'https://movie.douban.com/top250'

    # 模拟请求头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    }
    # 生成请求信息
    response = requests.get(url, headers=headers)

    #生成etree对象
    tree =  etree.HTML(response.text)

    #匹配src
    srcs =  tree.xpath('//ol[@class=\'grid_view\']/li//div[@class = \'pic\']/a/@href')
    #匹配name
    names = tree.xpath('//ol[@class=\'grid_view\']/li//div[@class = \'pic\']/a/img/@alt')

    for src,name in zip(srcs,names):
        item={
            'src':src,
            'name':name,
        }

        items.append(item)
    return items

if __name__ == '__main__':
    print(main())