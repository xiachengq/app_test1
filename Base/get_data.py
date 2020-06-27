import os,yaml
class GetData:
    """读取测试数据"""
    @classmethod
    def get_yaml_data(cls,name):
        """
        读取yaml数据
        :param name: 文件名字
        :return: yaml文件数据
        """
        # Data目录是固定的，如果你是用其他的，需要变更
        with open("./Data" + os.sep + name, "r",encoding="utf-8") as f:
            # yaml读取文件
            return yaml.safe_load(f)
