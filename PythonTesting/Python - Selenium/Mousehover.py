from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote import switch_to

driver = webdriver.Chrome(executable_path="F:\\Python-Seleniumjars\\chromedriver.exe")

#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#actions = ActionChains(driver)
#menu = driver.find_element_by_id("mousehover")
#actions.move_to_element(menu).perform()

#childElement = driver.find_element_by_link_text("Reload")
#actions.move_to_element(childElement).click().perform()


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
actions = ActionChains(driver)

#actions.double_click(driver.find_element_by_id("double-click")).perform()
actions.context_click(driver.find_element_by_id("double-click")).perform()
actions.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
