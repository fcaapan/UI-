# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_untitled(self):
        self.driver.get("https://www.bilibili.com/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-search-input").send_keys("红警HBK08")
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".nav-search-input").send_keys(Keys.ENTER)
        self.vars["win220"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win220"])
        element = self.driver.find_element(By.CSS_SELECTOR, ".col_3:nth-child(12) img")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.switch_to.window(self.vars["win220"])
        element = self.driver.find_element(By.CSS_SELECTOR, ".col_3:nth-child(6) .bili-video-card__info--date")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".video > .video-list").click()
        element = self.driver.find_element(By.LINK_TEXT, "下载客户端")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.window(self.vars["root"])
        element = self.driver.find_element(By.LINK_TEXT, "游戏中心")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".bili-video-card__info--ad")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".top-btn-wrap").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bili-feed4-layout").click()

