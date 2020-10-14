from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    productName = product.find_element_by_xpath("div/h4").text
    if productName == "Nokia Edge":
        product.find_element_by_xpath("div[2]/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()

title = driver.find_element_by_css_selector("h4[class='media-heading'] a").text
assert title == "Nokia Edge"

driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='suggestions']/ul")))

SearchResults = driver.find_elements_by_xpath("//div[@class='suggestions']/ul").text
for item in SearchResults:
    print(item)

#assert "ind" in item
