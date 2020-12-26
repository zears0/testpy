from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.settrade.com/settrade/home")
assert "SETTRADE" in driver.title
elem = driver.find_element_by_id("quote")
elem.send_keys("PTT")
elem.send_keys(Keys.RETURN)
time.sleep(2)
assert "SETTRADE" in driver.title
elem = driver.find_element_by_link_text("ราคาย้อนหลัง")
elem.click()
time.sleep(2)
assert "SETTRADE" in driver.title
print("Closing Price of The Last 3 Days")
elem = driver.find_element_by_xpath("//*[@class=\"table-responsive\"]/table/tbody/tr/td[6]")
print(elem.text)
elem = driver.find_element_by_xpath("//*[@class=\"table-responsive\"]/table/tbody/tr[2]/td[6]")
print(elem.text)
elem = driver.find_element_by_xpath("//*[@class=\"table-responsive\"]/table/tbody/tr[3]/td[6]")
print(elem.text)
driver.close()
