from basepage.basepage import BasePage
from selenium.webdriver.common.by import By

from config import URL


class HomePage(BasePage):
    # 哔哩哔哩首页面对象
    # 元素对象： 用户名输入框、密码输入框、验证码输入框、登录按
    # 定义实例属性层
    def __init__(self):
        super().__init__()
        self.search_input = (By.CSS_SELECTOR, ".nav-search-input")  # 搜索框
        self.search_btn = (By.CSS_SELECTOR, ".nav-search-btn")  # 搜索按钮
        self.next_page_btn = (By.CSS_SELECTOR, ".pager .next")  # 下一页按钮
        self.video_items = (By.CSS_SELECTOR, ".video-item a.title")  # 视频链接

    def search(self, search_str):
        """
        搜索指定的字符串。
        :param search_str: 表示输入的搜索内容
        """
        self.input_text(self.get_element(self.search_input), search_str)  # 输入搜索内容
        self.get_element(self.search_btn).click()  # 点击搜索按钮

    def scroll_down(self):
        """
        滚动到页面底部。
        """
        self.scroll_to_bottom()

    def click_next_page(self):
        """
        点击下一页按钮。
        """
        self.get_element(self.next_page_btn).click()  # 点击下一页按钮

    def click_first_video(self):
        """
        点击第一个视频链接。
        """
        first_video = self.get_element(self.video_items)
        first_video.click()  # 点击第一个视频

if __name__ == '__main__':
    # 实例化 BasePage 对象
    home_page = HomePage()
    home_page.open(URL)  # 打开哔哩哔哩首页

    # 执行搜索操作
    home_page.search("Python 教程")


    # 点击第一个视频
    home_page.click_first_video()

    # 关闭浏览器
    home_page.driver.quit()