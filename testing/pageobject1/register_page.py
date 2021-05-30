# 开发人员： 曾祥茂
# 日期： 2021/03/31
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver
#注册信息
    def register_sucdess(self):
        self.driver.find_element(By.ID,"corp_name").send_keys("aaaaaaa")
        self.driver.find_element(By.ID,"manager_name").send_keys("bbbbbbbbb")
        self.driver.find_element(By.ID,"register_tel").send_keys("13222222222")
        self.driver.find_element(By.ID,"submit_btn").click()
        return True

    def register_fail(self):
        self.driver.find_element(By.ID,"corp_name").send_keys("aaaaaaa")
        self.driver.find_element(By.ID,"manager_name").send_keys("bbbbbbbbb")
        self.driver.find_element(By.ID,"register_tel").send_keys("13222222222")
        self.driver.find_element(By.ID,"submit_btn").click()
        return True