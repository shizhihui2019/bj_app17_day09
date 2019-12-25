# 5+++++++++++++++++==
import pytest

from Base.getDriver import get_android_driver
from Page.newPage import Page


class TestSms:

    def setup_class(self):
        # ����driver
        self.driver = get_android_driver("com.android.mms",".ui.ConversationList")
        # ʵ����ͳһ�����
        self.page = Page(self.driver)



    '''�ر�driver'''
    def teardown_class(self):
        self.driver.quit()

    '''��������½�ҳ�� --�Զ�����1��'''
    @pytest.fixture(scope = 'clsaa',autouse=True)
    def goto_new_sms_page(self):
        # ��ҳ����½�
        self.page.get_home_page().click_new_sms_btn()
        # �½�ҳ�������ֻ���
        self.page.get_new_page().send_phone("1330000088888")

    '''���Ͷ��Ų��Է���'''
    def test_send_smsa(self,text):
        # ���Ͷ���
        self.page.get_new_page().send_sms(text)
        # ���Խ��
        assert text in self.page.get_new_page().get_sms_result()


