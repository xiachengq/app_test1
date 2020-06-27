from Base.base import Base
from Page.ele import Ele


class SettingPage(Base):
    """设置页面操作"""

    def __init__(self):
        super().__init__()

    def click_search(self):
        # 点击搜索
        self.click_btn(Ele.search_id)
