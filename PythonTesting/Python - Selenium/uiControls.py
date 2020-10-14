from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


assert driver.find_element_by_css_selector("#show-textbox").is_displayed()

driver.find_element_by_css_selector("#hide-textbox").click()

assert  driver.find_element_by_css_selector("#show-textbox").is_displayed()























