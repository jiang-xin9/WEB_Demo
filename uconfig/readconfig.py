# -->>>清安<<<---
import os

class Config:
    ''' 项目下所有文件的相对路径'''
    Base_Path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..')
    Base_Data = Base_Path + r'\Rdata\case01.xlsx'
    ChromeDriver_Path = Base_Path + r'\lib\chromedriver.exe'
    FirefoxDriver_Path = Base_Path + r'\lib\geckodriver.exe'
    Base_log = Base_Path + r'\LLog'

readConfig = Config()