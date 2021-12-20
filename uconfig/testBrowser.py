# -->>>清安<<<---
import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from uconfig.readconfig import readConfig
from Rcase.readexcel import parse_case
from uconfig.waitloc import Waitloc
from LLog.get_log import log_info
import allure
# # 初始化driver
# driver = webdriver.Firefox(executable_path=readConfig.FirefoxDriver_Path)
# driver.implicitly_wait(2)  # 设置元素的全局等待时间为2秒，当操作元素时，元素2秒内未出现就抛出异常
# driver.maximize_window()  # 最大化浏览器窗口



class Testcase():
    pre = parse_case(readConfig.Base_Data)

    # 调用parse_case方法，对文件名为:“自动化测试用例.xlsx”里的数据进行解析，解析为[{},{}]列表的形式，这样pytest才能够识别
    @pytest.mark.parametrize("data", pre)
    @allure.step
    # data为excel中的每行记录（步骤）转换成的pytest能识别的代码：{'action': 'send_keys', 'location_method': 'XPATH', 'path': '//*[@id="account"]', 'value': 'admin'}
    def test_run_case(self,data,supdriver):
        ele, location_method = data.get('ele'), data.get('location_method')  # 获取元素地址、定位方法
        action, value = data.get('action'), data.get('value')  # 获取要执行的操作、和操作的值(例如；send_keys的value)
        location = data.get('loc')
        if ele:
            if location_method:
                ffox = supdriver.find_element(getattr(By, location_method), ele)
                log_info.info(f'判断元素是：{getattr(By, location_method),ele}')
                if location:
                    getattr(Waitloc,location),(ffox)
                # 下面为封装的具体操作，根据excel表获取的不同则执行不同的操作
                if action == 'click':  # 如果要执行的操作等于click则执行点击事件
                    ffox.click()
                elif action == 'send_keys' and value:
                    ffox.send_keys(value)
        elif value:  # 没有元素路径则代表执行的操作不需要元素路径，所以下面封装的操作都是不需要元素路径的
            if action == 'sleep':  # 强制等待
                time.sleep(float(value))
            else:
                # 通过反射封装操作，根据excel表获取的不同则执行不同的操作
                getattr(supdriver, action)(value) if value else getattr(supdriver, action)()
        else:
            return False
