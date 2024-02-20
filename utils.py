# 定义工具类
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from config import URL

# from appium import webdriver as appdriver


class UtilsDriver:
    _driver = None  # 驱动标识
    # 定义获取驱动的方法
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            service =Service("drivers/chromedriver.exe")
            options= Options()
            cls._driver = webdriver.Chrome(service=service,options=options)
            cls._driver.get(url=URL)
            cls._driver.maximize_window()
        return cls._driver

    # 定义驱动的退出
    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None



    # 定义获取app的驱动
    @classmethod
    def get_app_driver(cls):
        desired_caps = dict()  # {"platformName":'Android'} # 定义了一个空字典

        # 被测试手机设备系统型号
        desired_caps['platformName'] = 'Android'
        # 被测试手机系统的版本号,可以写大的版本号,不能写错
        desired_caps['platformVersion'] = '13.1'
        # 被测试手机的设备号。如果只连接了一个手机或模拟器，可以用****来表示
        desired_caps['deviceName'] = 'emulator-5554'
        # 被测试的APP的包名
        desired_caps['appPackage'] = 'com.tpshop.malls'
        # 被测试的APP的启动名(启动名属于界面名，也就是app打开的第一个界面名称)
        desired_caps['appActivity'] = 'com.bilibili.malls.SPMainActivity'
        if cls._app_driver is None:
            # 创建app的驱动
            cls._app_driver = appdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return cls._app_driver

    # 定义app驱动的退出
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls._app_driver.quit()
            cls._app_driver = None


