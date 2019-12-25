from Page.homePage import HomePage
from Page.newPage import NewPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    '''���ض�����ҳʵ����'''

    def get_home_page(self):
        return HomePage(self.driver)

    '''�����½�ҳ�����'''

    def get_new_page(self):
        return NewPage(self.driver)
