# 开发人员： 曾祥茂
# 日期： 2021/03/31
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from testing.pageobject1.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver:WebDriver):
#WebDriver给出find的类型提示
        self.driver = driver
    #扫码
    def scan(self):
        pass


    #进入到注册页

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        return RegisterPage(self.driver)


