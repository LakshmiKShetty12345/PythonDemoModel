from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")

driver.get("https://login.salesforce.com/?locale=in")

driver.find_element_by_css_selector("#username").send_keys("Lakshmi")

driver.find_element_by_css_selector(".password").send_keys("Shetty")

driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_partial_link_text("Forgot Your").click()

driver.find_element_by_xpath('//a[text()="Cancel"]').click()

