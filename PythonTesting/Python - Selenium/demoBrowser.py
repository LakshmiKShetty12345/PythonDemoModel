
from selenium import webdriver

#driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="F:\\Python-Seleniumjars\\geckodriver.exe")
driver = webdriver.Ie(executable_path="F:\\Python-Seleniumjars\\IEDriverServer.exe")
driver.get('https://rahulshettyacademy.com/#/index')
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.get("http://rahulshettyacademy.com/AutomationPractice")
driver.minimize_window()
driver.back()
driver.refresh()

driver.close()
