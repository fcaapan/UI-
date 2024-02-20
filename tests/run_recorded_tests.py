from selenium import webdriver
import time

# 启动 Chrome 浏览器
driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

# 执行录制的测试脚本
def run_test_case(test_case_file):
    driver.get('http://www.example.com')  # 打开测试网站
    driver.maximize_window()  # 最大化窗口

    # 读取录制的测试脚本文件
    with open(test_case_file, 'r', encoding='utf-8') as file:
        test_script = file.read()

    # 执行录制的测试脚本
    driver.execute_script(test_script)

    time.sleep(5)  # 等待一段时间，以便观察测试结果

# 执行所有录制的测试脚本
def run_all_test_cases():
    test_files = ['tests/recorded_scripts/test_case1.side', 'tests/recorded_scripts/test_case2.side']
    for test_file in test_files:
        run_test_case(test_file)

# 执行所有录制的测试脚本
run_all_test_cases()

# 关闭浏览器
driver.quit()