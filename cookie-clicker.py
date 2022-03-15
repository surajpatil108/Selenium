from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


chromedriver_parth = "/home/suraj/Downloads/chromedriver"

options = webdriver.ChromeOptions()
s = Service(chromedriver_parth)
driver = webdriver.Chrome(service=s, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")

timeout = time.time() + 60*0.5

period = time.time() + 5


while True:
    cookie.click()
    score_board = driver.find_element(By.ID, "money").text
    cookies = int(score_board)
    speed = driver.find_element(By.ID, "cps")
    speed_number = int(speed.text.split(":")[1])

    if cookies > 100:
        # grandma = WebDriverWait(driver, 11).until(
        #     EC.element_to_be_clickable((By.ID, "buyGrandma")))
        driver.find_element(By.ID, "buyGrandma").click()

        cursor = WebDriverWait(driver, 11).until(
            EC.element_to_be_clickable((By.ID, "buyCursor")))
        driver.find_element(By.ID, "buyCursor").click()
        break

    if time.time() > timeout:
        print(cookies)
        driver.quit()






