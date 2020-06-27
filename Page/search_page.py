from Base.base import Base
from Page.ele import Ele


class SearchPage(Base):
    """搜索页面操作"""
    def __init__(self):
        super().__init__()
    def send_texts(self,text):
        # 输入测试数据
        self.send_text(Ele.searches_id,text)
    def get_text(self):
        # 获取结果列表
        result = self.find_eles(Ele.get_search)
        # 返回列表结果
        return [i.text for i in result]
