
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
list2 = []

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='product-action']/button"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(list)


driver.find_element_by_css_selector("a[class='cart-icon'] img").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promocode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2)
assert list == list2

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_css_selector(".promocode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
#wait1 = WebDriverWait(driver,5)

wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discountAmount) < float(originalAmount)


print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")

sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
    print(sum)

TotalAmount = int(driver.find_element_by_css_selector("span.totAmt").text)
print(TotalAmount)

assert sum == TotalAmount

