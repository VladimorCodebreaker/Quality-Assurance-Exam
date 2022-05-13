from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Safari()
driver.get("https://www.cdjapan.co.jp")

select = Select(driver.find_element_by_id("suggester_qtype"))

select.select_by_visible_text("All CD")

driver.sleep(3)
driver.quit