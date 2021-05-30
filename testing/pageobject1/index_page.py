# 开发人员： 曾祥茂
# 日期： 2021/03/31
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

from testing.pageobject1.login_page import LoginPage
from testing.pageobject1.register_page import RegisterPage

from time import sleep


class IndexPage():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")


        self.driver.maximize_window()

    # 进入登录页面
    def goto_login(self):
        # click logxin
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        sleep(2)

        # return loginpage
        # self.driver.execute_script("document.documentElement.scrollTop=10000")
        # sleep(2)
        return LoginPage(self.driver)

    # 进入注册页
    def goto_register(self):
        # click signup

        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        sleep(2)

        return RegisterPage(self.driver)