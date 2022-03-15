from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

chromedriver_parth = "/home/suraj/Downloads/chromedriver"

options = webdriver.ChromeOptions()
s = Service(chromedriver_parth)
driver = webdriver.Chrome(service=s, options=options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.click()
first_name.send_keys("Suraj Bhau")

last_name = driver.find_element(By.NAME, "lName")
last_name.click()
last_name.send_keys("Patil Bhau")

email = driver.find_element(by=By.NAME, value="email")
email.click()
email.send_keys("surajrajput@gmail.com")

button = driver.find_element(By.XPATH, '//*[@type="submit"]')
button.click()

print("success")

driver.quit()
