# -->>>清安<<<---
# -->>>清安<<<---
import logging
import time
from uconfig.readconfig import readConfig

class Log_object():
    def __init__(self):  # 构造函数初始化日志器
        self.log = logging.getLogger(name='TestFramework')
        self.log.setLevel(level=logging.DEBUG)
        fmt_log = '[时间:%(asctime)s  日志级别:%(levelname)s  文件名:%(filename)s  第%(lineno)d行:>>>日志信息:%(message)s]'
        self.formatter = logging.Formatter(fmt_log)
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = readConfig.Base_log


    def add_StreamHandler(self):  # 控制台处理器
        # 创建并初始化处理器
        self.sh = logging.StreamHandler()
        # 设置处理器级别
        self.sh.setLevel(level=logging.INFO)
        # 处理器添加格式器
        self.sh.setFormatter(fmt=self.formatter)
        # 日志器添加处理器
        self.log.addHandler(hdlr=self.sh)

    def add_FileHandler(self):  # 文件处理器
        self.fh = logging.FileHandler(filename='{0}\{1}.log'.format(self.log_path,self.log_time))
        self.fh.setLevel(level=logging.INFO)
        self.fh.setFormatter(fmt=self.formatter)
        self.log.addHandler(hdlr=self.fh)

    def get_log(self):
        self.add_StreamHandler()
        self.add_FileHandler()
        return self.log


log_info = Log_object().get_log()


