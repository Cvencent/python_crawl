from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 设置
from selenium.webdriver.chrome.options import Options
import time

# selenium简单示例
def main():
    # 创建设置对象
    options = Options()
    # 设置无头模式
    options.add_argument('--headless')

    url = 'https://www.baidu.com/'

    # 创建一个webdriver谷歌浏览器器对象,需要下载驱动
    driver = webdriver.Chrome('C:\\Users\\vencent\\Downloads\\chromedriver_win32\\chromedriver.exe',options =options )
    # 发送请求
    driver.get(url)
    # 等待3秒
    time.sleep(3)
    # 找到输入框
    input_b = driver.find_element_by_id('kw')
    time.sleep(1)
    # 输入‘python’
    input_b.send_keys('python')
    # 回车
    input_b.send_keys(Keys.RETURN)
    # 等待3秒
    time.sleep(3)
    # 关闭浏览器
    driver.close()

if __name__ == '__main__':
    main()



