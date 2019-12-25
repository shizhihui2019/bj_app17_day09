from Page.homePage import HomePage
from Page.newPage import NewPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    '''返回短信首页实例化'''

    def get_home_page(self):
        return HomePage(self.driver)

    '''返回新建页面对象'''

    def get_new_page(self):
        return NewPage(self.driver)
