
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class google_login:
    def google_login(driver, email, password, callback):
        driver.get("https://dev-portal.sphere-meta.com/zh-tw/home")
        # 等待網頁加載
        time.sleep(2)
        # 找到包含特定文字的按鈕元素
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), '登入 / 註冊')]")
        # 點擊登入/註冊按鈕
        login_button.click()
        # 等待搜尋結果加載
        time.sleep(2)
        # 找到使用 Google 繼續按鈕元素
        google_button = driver.find_element(By.XPATH,"//p[contains(text(), '使用 Google 繼續')]/ancestor::button")
        google_button.click()
        # 等待所有窗口加載完成
        time.sleep(2)
        # 獲取所有窗口的 handle
        all_handles = driver.window_handles
        # 切換到新打開的窗口
        new_window = all_handles[-1]  # 假設新窗口是最後一個
        driver.switch_to.window(new_window)
        # 在新窗口中找到帳號輸入框，並輸入帳號
        email_input = driver.find_element(By.XPATH, "//input[@type='email']")
        email_input.send_keys(email)  # 替換為你的 Gmail 帳號
        # 找到下一步按鈕並點擊
        next_button = driver.find_element(By.XPATH, "//div[@id='identifierNext']")
        next_button.click()
        # 等待一下，然後輸入密碼
        time.sleep(2)
        # 在新窗口中找到密碼輸入框，並輸入密碼
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(password)  # 替換為你的 Gmail 密碼

        # 找到登入按鈕並點擊
        login_button = driver.find_element(By.XPATH, "//div[@id='passwordNext']")
        login_button.click()
        time.sleep(10)
        # 等待頁面跳轉（假設這裡等待10秒，視情況調整等待時間）
        callback()

