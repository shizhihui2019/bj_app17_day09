import yaml

# 读取文件

with open("./value2.yml", "r", encoding="utf-8") as  f:
    # 加载文件
    data = yaml.safe_load(f)

    # 打印数据
    print("data:{}".format(data))

    # 打印类型
    # print("类型:{}".format(data))
    # print("类型:{}".format(type(data.get("value"))))
    # print("类型:{}".format(type(data.get("value16"))))
    # print("类型:{}".format(type(data.get("value17"))))
    # print("类型:{}".format(type(data.get("value18"))))

