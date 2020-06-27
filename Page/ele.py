from selenium.webdriver.common.by import By


class Ele:
    """设置页面元素"""
    # 搜索元素
    search_id = (By.ID, "com.android.settings:id/search")

    """搜索页面元素"""
    # 搜索输入元素
    searches_id = (By.ID, "android:id/search_src_text")
    # 获取结果元素
    get_search = (By.ID, "com.android.settings:id/title")
