# -->>>清安<<<---

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import supdriver
from selenium.webdriver.common.action_chains import ActionChains



class Waitloc:

    """判断某个元素是否存在"""
    def presence_of_element_located(self, ffox):
        WebDriverWait(supdriver, 5, 0.5).until(EC.presence_of_element_located(ffox))

    """判断某个元素是否可以被点击"""
    def element_to_be_clickable(self, ffox):
        WebDriverWait(supdriver, 5, 0.5).until(EC.element_to_be_clickable(ffox))

    """判断某个元素中是否不存在"""
    def invisibility_of_element_located(self, ffox):
        WebDriverWait(supdriver, 5, 0.5).until(EC.invisibility_of_element_located(ffox))

    """元素可以被选择"""
    def located_selection_state_to_be(self, ffox):
        WebDriverWait(supdriver, 5, 0.5).until(EC.element_located_selection_state_to_be(ffox, is_selected="元素不可被选择"))

    """鼠标悬浮在某个元素上"""
    def action_move_to_element(self, ffox):
        ActionChains(supdriver).move_to_element(ffox).perform()

    """鼠标左键双击"""
    def action_double_click(self,ffox):
        ActionChains(supdriver).double_click(ffox).perform()

    """"""


