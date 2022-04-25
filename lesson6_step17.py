import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("div .trollface")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

try:
  def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))
 
  x_element = browser.find_element_by_id('input_value').text
  x = calc(x_element)

  input1 = browser.find_element_by_id('answer')
  input1.send_keys(x)

  button2 = browser.find_element_by_class_name("btn")
  button2.click()

finally:

  time.sleep(10)
  browser.quit()