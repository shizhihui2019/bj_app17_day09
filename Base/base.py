from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def search_ele(self, loc, timeout=5, poll=1):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)
        :param timeout: 搜索元素超时时间
        :param poll: 搜索间隔
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))


    '''定为一组元素'''
    def search_eles(self, loc, timeout=5, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))


    '''点击元素'''
    def click_ele(self, loc, timeout=5, poll=1):
        self.search_ele(loc, timeout, poll).click()


    '''输入文本内容'''
    def send_ele(self, loc, text, timeout=5, poll=1):
        # 定位
        input_text = self.search_ele(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)
