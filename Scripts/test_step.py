import allure
class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER) # 最重要的用例
    @allure.step("我是测试步骤名字")
    def test_001(self):
        """添加测试步骤"""
        allure.attach("我是步骤描述的内容","附件名字")

    @allure.severity(allure.severity_level.CRITICAL)  # 比较重要的用例
    def test_002(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)  # 正常的用例
    def test_003(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)  # 比一般低一些用例
    def test_004(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)  # 可以忽略的用例
    def test_005(self):
        assert True