# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Lenskart homepage
driver.get("https://www.lenskart.com/")
time.sleep(10)

# Closing the initial popup if it appears
try:
    close_popup = driver.find_element(By.CLASS_NAME, "cross")
    close_popup.click()
except:
    pass

# Finding the eyeglasses button and clicking on it
eyeglasses_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[1]/section/div/center/div/div[1]")
eyeglasses_button.click()

# Waiting for the eyeglasses page to load
time.sleep(5)

# Selecting a pair of eyeglasses from the search results
# In this example, we're clicking on the first product
eyeglasses_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[2]")
eyeglasses_link.click()

# Waiting for the eyeglasses details page to load
time.sleep(5)

# Switching back to the default content (in case there are iframes)
driver.switch_to.default_content()

# Clicking on the "BUY NOW" button using the parent class
buy_now_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="AddToCartButtonWrapper--kg9kcq hNgCxJ"]//button[@class="PrimaryButtonWrapper--1g9ssp8 pVWCF"]'))
)
buy_now_button.click()

# Waiting for the checkout page to load
time.sleep(5)

# Verifying that the checkout page has loaded
assert "Checkout" in driver.title

# Closing the webdriver
driver.quit()
