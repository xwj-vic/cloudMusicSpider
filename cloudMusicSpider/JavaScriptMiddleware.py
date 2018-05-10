from selenium import webdriver
import selenium.webdriver.support.ui as ui
from scrapy.http import HtmlResponse


# 采用中间件结合selenium
class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "CloudMusicSpider":
            # 指定使用的浏览器
            driver = webdriver.Chrome('/home/xuweijie/driver/chromedriver')
            driver.get(request.url)
            # 移动到id="g_iframe"的iframe
            driver.switch_to.frame('g_iframe')
            wait = ui.WebDriverWait(driver, 15)
            if wait.until(lambda driver: driver.find_element_by_id('m-pl-container')):
                body = driver.page_source
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8',
                                request=request)
        else:
            return
