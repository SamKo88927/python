# Your test code goes here
# This is a placeholder for your test case
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class test_checkout_process:
    def test_checkout_process(driver):
        # driver.get("https://dev-portal.sphere-meta.com/zh-tw/home")
        time.sleep(10)
        next_button = driver.find_element(By.CLASS_NAME, "nft-card--content") # You can adjust this locator
        ActionChains(driver).move_to_element(next_button).perform()
        next_button.click()

        wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        wait.until(EC.url_changes)
        time.sleep(5)
        # Click the "前往去購買" button
        Purchase_button = driver.find_element(By.XPATH, "//button[contains(text(), '前往去購買')]")
        ActionChains(driver).move_to_element(Purchase_button).perform()
        Purchase_button.click()
        time.sleep(5)  # Assuming you're waiting for the page to load after clicking

        # Scroll down after a delay of 10 seconds
  

        screenName = driver.find_element(By.ID, "screenName")
        # Check if screenName input field is empty, if so, fill it with a placeholder value
        if not screenName.get_attribute("value"):
            placeholder_text = "John Doe"  # Replace this with your desired placeholder
            screenName.send_keys(placeholder_text)
        # oversea
        overseas_button = driver.find_element(By.XPATH, "//button[contains(text(), 'overseas')]")
        overseas_button.click()
        Purchase_button = driver.find_element(By.XPATH, "//button[contains(text(), '繼續')]")
        Purchase_button.click()
        time.sleep(5)

        # 還有問題
        paypal_button = driver.find_element(By.XPATH, "//dev[contains(text(), 'pay with')]/ancestor::button")
        paypal_button.click()
        time.sleep(10)
        # Find the PayPal button element by its class name
        paypal_button = driver.find_element(By.CSS_SELECTOR, "div.paypal-button")

        # Get or interact with the attributes of the PayPal button element
        # For instance, you can get the aria-label attribute using get_attribute method
        aria_label = paypal_button.get_attribute("aria-label")
        print("aria-label attribute:", aria_label)

        print("繼續操作")