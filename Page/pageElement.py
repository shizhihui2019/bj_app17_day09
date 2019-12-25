# 1++++++++++++++


'''管理所有页面元素'''
from selenium.webdriver.common.by import By


class PageElement:
    '''短信列表页面'''
    home_sms_new_btn_id = (By.ID, "com.android.mms:id/action_compose_new")

    '''新建短信页面'''
    # 短信接收人
    new_sms_recv_phone_id = (By.ID, "com.android.mms:id/recipients_editor")
    # 短信输入框
    new_sms_send_text_id = (By.ID, "com.android.mms:id/embedded_text_editor")
    # 发送按钮
    new_sms_send_btn_id = (By.ID, "com.android.mms:id/send_button_sms")

    # 已发送列表
    new_sms_results_ids = (By.ID, "com.android.mms:id/text_view")
