import yaml, os


class GetData:

    # ��
    # ����̨����:python-->import os-->os.sep-->��ȡϵͳ·���ָ���,��Ϊunix�ָ���Ϊ:"/" window "\"
    # ����yaml�ļ�����
    # yml_name:yml_name:yaml�����ļ�����
    def get_yml_data(self, yml_name):
        with open("./Data" + os.sep + yml_name, "r", encoding="GBK") as f:
            # �����ļ� --> ����
            return yaml.safe_load(f)

    def get_json_data(self):
        pass
