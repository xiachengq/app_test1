from appium import webdriver


class Driver:
    """封装driver驱动器"""
    app_driver = None

    @classmethod
    def get_driver(cls):
        """声明手机驱动对象"""
        if not cls.app_driver:
            # 启动参数
            desired_caps = {
                "platformName": "Android",
                "piatformVersion": "5.1",
                "deviceName": "sanxing",
                "appPackage": "com.android.settings",
                "appActivity": ".Settings"

            }
            cls.app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            return cls.app_driver

    @classmethod
    def quit_driver(cls):
        """关闭driver驱动对象"""
        if cls.app_driver != None:
            cls.app_driver.quit()
            cls.app_driver = None
