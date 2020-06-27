from Page.search_page import SearchPage
from Page.setting_page import SettingPage


class ObjectBase:
    """返回所有操作实例化对象"""

    @classmethod
    def get_setting(cls):
        # 返回设置页面对象
        return SettingPage()

    @classmethod
    def get_search(cls):
        # 返回搜索页面对象
        return SearchPage()
