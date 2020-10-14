from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_id("exampleCheck1").click()

driver.find_element_by_css_selector("input[name='name']").send_keys("Lakshmi")


driver.find_element_by_xpath("//input[@type = 'submit']").click()

message = driver.find_element_by_class_name("alert-success").text
assert "Success" in message


#dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)




