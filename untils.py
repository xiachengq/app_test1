"""定义读取json测试数据并且组织成parameterized.expand所要求的数据格式函数"""
# 1.定义测试数据的函数
import json


def build_testData(file_path):
    # 2.测试完整数据存储到空格列表
    test_dict = []
    # 3.读取文件
    with open(file_path,encoding="utf-8") as f:
        # 4.读取json文件的完整数据并且自动化装维python字典数据
        json_str = json.load(f)
        # 5.获取一层键值
        for i in json_str.values():
            # 6.获取键值所有键值
            test_dict.append(list(i.values()))
    # 返回组织好的测试数据
    return test_dict
