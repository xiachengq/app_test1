import allure
import pytest
from Base.base_driver import Driver
from Base.get_data import GetData
from Base.object import ObjectBase
from config import BASE_PATH
from untils import build_testData
from parameterized import parameterized
def search_data():
    sun_list = []
    data = GetData.get_yaml_data("search_data.yaml")
    for i in data.values():
        sun_list.append((i.get("search_text"),i.get("expect")))
    print("sun_list",sun_list)
    return sun_list









class TestSearch:
    def setup_class(self):
        Driver.get_driver()

    def teardown_class(self):
        Driver.quit_driver()

    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击搜索按钮"""
        ObjectBase.get_setting().click_search()

    # @parameterized.expand(build_testData(BASE_PATH + "/Data/search_text.json"))
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("操作搜索测试用例")
    @pytest.mark.parametrize("search_text, expect",search_data())
    def test_search(self, search_text, expect):
        # 输入内容
        allure.attach("搜索框输入测试数据","输入步骤")
        ObjectBase.get_search().send_texts(search_text)
        # 获取结果进行断言
        allure.attach("返回结果列表进行断言","断言")
        assert expect in ObjectBase.get_search().get_text()
