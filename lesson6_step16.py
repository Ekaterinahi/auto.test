import math, time
from selenium import webdriver

link = " http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

element1 = browser.find_element_by_css_selector("[type='submit']")
element1.click()

confirm = browser.switch_to.alert
confirm.accept()

try:
  
   
  def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))


  x_element = browser.find_element_by_css_selector("#input_value")
  x = x_element.text
  y = calc(x)

  element1 = browser.find_element_by_css_selector('#answer')
  element1.send_keys(y)

  option2 = browser.find_element_by_css_selector("[type='submit']")
  option2.click()

finally:

  time.sleep(20)
  browser.quit()