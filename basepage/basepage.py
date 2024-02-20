# 定义页面操作基类
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver


class BasePage:
    # 定义初始化方法
    def __init__(self):
        self.driver = UtilsDriver.get_driver()  # 获取后台系统的驱动

    # 定义获取元素对象的方法
    def get_element(self,location) -> WebElement:
        """
        :param location: 表示的是元素的定位信息
            ID 定位：通过元素的 id 属性定位。
            Class Name 定位：通过元素的 class 属性定位。
            Tag Name 定位：通过元素的标签名定位。
            Link Text 定位：通过链接文本定位完整的 <a> 标签元素。
            Partial Link Text 定位：通过链接的部分文本定位 <a> 标签元素。
            CSS Selector 定位：通过 CSS 选择器定位元素。
            XPath 定位：通过 XPath 表达式定位元素。
        :return: 返回的是一个元素对象WebElement
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(lambda x:x.find_element(*location))

    # 定义元素的输入操作
    def input_text(self, element, text):
        """
        :param element: 表示的是元素对象
        :param text: 表示的是要输入的文本内容
        :return:
        """
        element.clear()
        element.send_keys(text)

    # 定义下拉选择框操作
    def select_choice_value(self,element,value):
        """
        :param element: 表示的是下拉框元素对象
        :param value: 表示的是选项的value属性值
        :return:
        """
        time.sleep(1)
        select = Select(element)
        select.select_by_value(value)


   # 定义鼠标悬停操作
    def hover_element(self, element,tooltip_locator=None):
        """
        :param element: 表示的是元素对象
        :param tooltip_locator: 表示的是工具提示的定位信息
        :return: 返回的是工具提示的文本内容
        """
        ActionChains(self.driver).move_to_element(element).perform()
        if tooltip_locator:
            tooltip_element = self.get_element(tooltip_locator)
            return tooltip_element.text

    # 定义鼠标右击操作
    def context_click_element(self, element):
        """
        :param element: 表示的是元素对象
        :return:
        """
        ActionChains(self.driver).context_click(element).perform()

    # 定义鼠标双击操作
    def double_click_element(self, element):
        """
        :param element: 表示的是元素对象
        :return:
        """
        ActionChains(self.driver).double_click(element).perform()

    # 定义鼠标拖拽操作
    def drag_and_drop_element(self, source_element, target_element):
        """
        :param source_element: 表示的是要拖拽的源元素对象
        :param target_element: 表示的是目标元素对象
        :return:
        """
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    # 定义切换到最新打开窗口的方法
    def switch_to_new_window(self):
        """
        切换到最新打开的窗口。
        :return: 返回新窗口的标题
        """
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        return self.driver.title

    def switch_to_frame(self, frame_reference):
        """
        :param frame_reference: frame的索引、名称或WebElement对象
        切换到指定的frame。
        """
        self.driver.switch_to.frame(frame_reference)
        frame_id = frame_reference.get_attribute("id")
        self.driver.switch_to.frame(frame_reference)
        return frame_id


    # 定义切换回主文档的方法
    def switch_to_default_content(self):
        """
        切换回主文档。
        """
        self.driver.switch_to.default_content()


    # 定义截屏操作的方法
    def take_screenshot(self, file_name):
        """
        :param file_name: 截屏文件的名称，包括路径
        进行截屏操作，并将截图保存到指定的文件。
        """
        # 确保截图保存的目录存在
        directory = os.path.dirname(file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.driver.save_screenshot(file_name)

    #定义刷新当前页面。
    def refresh_page(self):
        """
        刷新当前页面。
        """
        self.driver.refresh()

    def scroll_to_bottom(self):
        """
        滚动到页面底部。
        """
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def execute_script(self, script, *args):
        """
        执行JavaScript脚本。
        :param script: 要执行的JavaScript代码
        :param args: 传递给JavaScript的参数
        :return: 脚本执行结果
        """
        return self.driver.execute_script(script, *args)



if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    # 假设 BasePage 类和其他必要的导入已经定义好了

    # 实例化 BasePage 对象
    base_page = BasePage()

    # 使用 CSS 选择器定位搜索输入框元素
    element_location = (By.CSS_SELECTOR, ".nav-search-input")
    element = base_page.get_element(element_location)
    # 在搜索输入框中输入文本
    base_page.input_text(element, "测试文本")

    # 假设 select_choice_value 方法需要一个下拉选择框元素，这里只是示例
    # 实际使用时应该传入正确的下拉选择框元素
    # 定位下拉选择框元素
    select_element = base_page.get_element(("ID", "select_element_id"))
    # 在下拉选择框中选择指定的选项值
    base_page.select_choice_value(select_element, "option_value")

    # 鼠标操作
    # 在搜索输入框元素上执行鼠标悬停操作
    base_page.hover_element(element)
    # 在搜索输入框元素上执行鼠标右击操作
    base_page.context_click_element(element)
    # 在搜索输入框元素上执行鼠标双击操作
    base_page.double_click_element(element)

    # 定位拖拽操作的源元素和目标元素
    source_element = base_page.get_element(("ID", "source_element_id"))
    target_element = base_page.get_element(("ID", "target_element_id"))
    # 执行拖拽操作，将源元素拖拽到目标元素的位置
    base_page.drag_and_drop_element(source_element, target_element)
    # 在搜索输入框元素上执行鼠标单击操作
    base_page.click_element(element)

    # 窗口和frame操作
    # 切换到最新打开的窗口
    base_page.switch_to_new_window()
    # 保存原始窗口的句柄
    original_window = base_page.driver.current_window_handle
    # 切换回原始窗口
    base_page.switch_to_original_window(original_window)
    # 定位frame元素并切换到该frame
    frame_reference = (By.ID, "frame_id")
    base_page.switch_to_frame(frame_reference)
    # 切换回主文档
    base_page.switch_to_default_content()

    # 页面操作
    # 刷新当前页面
    base_page.refresh_page()
    # 获取当前页面的URL
    current_url = base_page.get_current_url()
    # 获取当前页面的标题
    page_title = base_page.get_page_title()

    # JavaScript操作
    # 执行JavaScript脚本，弹出警告框
    base_page.execute_script("alert('执行JavaScript');")
    # 滚动到页面底部
    base_page.scroll_to_bottom()
    # 滚动到搜索输入框元素的位置
    base_page.scroll_to_element(element)

    # 等待操作
    # 等待搜索输入框元素可见
    base_page.wait_for_element_visible(element_location)
    # 等待搜索输入框元素可点击
    base_page.wait_for_element_clickable(element_location)

    # 截屏操作
    # 定义截屏文件的保存路径
    screenshot_path = "path/to/screenshots/screenshot.png"
    # 执行截屏操作并保存截图
    base_page.take_screenshot(screenshot_path)

    # 测试结束后关闭浏览器
    base_page.driver.quit()


