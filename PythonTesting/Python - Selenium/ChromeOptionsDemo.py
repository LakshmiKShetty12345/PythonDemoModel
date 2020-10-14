from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-error")



driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe",options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)