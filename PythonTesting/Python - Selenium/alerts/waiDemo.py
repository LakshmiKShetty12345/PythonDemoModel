import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='product-action']/button"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("a[class='cart-icon'] img").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()

driver.find_element_by_css_selector(".promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

print(driver.find_element_by_css_selector(".promoInfo").text)

