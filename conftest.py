"""根目录conftest"""
from uconfig.readconfig import readConfig
import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def supdriver():
    driver = webdriver.Firefox(executable_path=readConfig.FirefoxDriver_Path)
    driver.maximize_window()
    yield driver
    driver.quit()

