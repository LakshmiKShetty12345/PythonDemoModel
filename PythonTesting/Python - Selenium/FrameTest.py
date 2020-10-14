from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Now I Can automate test cases")
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)
#print(driver.find_element_by_tag_name("h3").text)
