from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)

url = "https://www.instagram.com/"
driver.get(url=url)
time.sleep(20)

xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'