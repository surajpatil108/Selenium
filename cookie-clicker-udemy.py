from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_parth = "/home/suraj/Downloads/chromedriver"

options = webdriver.ChromeOptions()
s = Service(chromedriver_parth)
driver = webdriver.Chrome(service=s, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#rightPanel div")

items_ids = [item.get_attribute("id") for item in items]
all_items_list = items_ids[1:-1]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        # all_prices_list = [all_price.text for all_price in all_prices]
        # print(all_prices_list)

        item_prices_list = []
        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                # print(cost)
                item_prices_list.append(cost)
        # print(item_prices)
        cookie_upgrade = {}
        for n in range(len(item_prices_list)):
            cookie_upgrade[item_prices_list[n]] = all_items_list[n]
        # print(cookie_upgrade)

        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
            # print(cookie_count)

        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        print(affordable_upgrades)


        highest_price_affordable_item = max(affordable_upgrades)
        # print(highest_price_affordable_item)
        to_purchase_id = affordable_upgrades[highest_price_affordable_item]
        # print(to_purchase_id)

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + 10

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break

driver.quit()
