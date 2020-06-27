from selenium.webdriver.support.wait import WebDriverWait

from Base.base_driver import Driver


class Base:
    def __init__(self):
        """调用Driver声明手机驱动对象"""
        self.driver = Driver.get_driver()

    def find_ele(self, loc, timeout=5, poll=1):
        """
        定义查找元素的方法
        :param loc: 查找的方法和元素
        :param timeout: 最大时间
        :param poll: 间隔
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_eles(self, loc, timeout=5, poll=1):
        """
        定义查找一组元素的方法
        :param loc: 查找的方法和元素
        :param timeout: 最大时间
        :param poll: 间隔
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_btn(self, loc, timeout=5, poll=1):
        """
        定义点击元素的方法
        :param loc: 查找的方法和元素
        :param timeout: 最大时间
        :param poll: 间隔
        :return:
        """
        self.find_ele(loc, timeout, poll).click()

    def send_text(self, loc, text, timeout=5, poll=1):
        """
        定义输入文本的方法
        :param loc: 查找的方法和元素
        :param text: 输入的内容
        :param timeout: 最大时间
        :param poll: 间隔
        :return:
        """
        input_text = self.find_ele(loc, timeout, poll)
        input_text.clear()
        input_text.send_keys(text)
