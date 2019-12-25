import yaml, os


class GetData:

    # 读
    # 控制台输入:python-->import os-->os.sep-->获取系统路径分隔符,因为unix分隔符为:"/" window "\"
    # 返回yaml文件数据
    # yml_name:yml_name:yaml数据文件名字
    def get_yml_data(self, yml_name):
        with open("./Data" + os.sep + yml_name, "r", encoding="GBK") as f:
            # 加载文件 --> 解析
            return yaml.safe_load(f)

    def get_json_data(self):
        pass
