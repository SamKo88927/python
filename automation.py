
from selenium import webdriver
from automation.login_tests.test_google_login import google_login
from automation.purchase_flow.test_checkout_process import test_checkout_process
# 創建一個Chrome瀏覽器實例
driver = webdriver.Chrome()
     # 定義完成登入後要執行的操作
def after_login():
    # 在登入完成後執行購買流程
    test_checkout_process.test_checkout_process(driver)

google_login.google_login(driver, "sam@sphere-meta.com", "sam56325", after_login)
# after_login()
