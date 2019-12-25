# 5+++++++++++++++++==
import pytest

from Base.getDriver import get_android_driver
from Page.newPage import Page


class TestSms:

    def setup_class(self):
        # 声明driver
        self.driver = get_android_driver("com.android.mms",".ui.ConversationList")
        # 实例化统一入口类
        self.page = Page(self.driver)



    '''关闭driver'''
    def teardown_class(self):
        self.driver.quit()

    '''进入短信新建页面 --自动运行1次'''
    @pytest.fixture(scope = 'clsaa',autouse=True)
    def goto_new_sms_page(self):
        # 首页点击新建
        self.page.get_home_page().click_new_sms_btn()
        # 新建页面输入手机号
        self.page.get_new_page().send_phone("1330000088888")

    '''发送短信测试方法'''
    def test_send_smsa(self,text):
        # 发送短信
        self.page.get_new_page().send_sms(text)
        # 断言结果
        assert text in self.page.get_new_page().get_sms_result()


