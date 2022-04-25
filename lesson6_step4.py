from selenium import webdriver
import math

link = " http://suninjuly.github.io/find_link_text"

try :
  browser = webdriver.Chrome()
  browser.get(link)
  a =str(math.ceil(math.pow(math.pi, math.e)*10000))
  link = browser.find_element_by_link_text("str(a)")
  link.click()

finally:
    
    time.sleep(15)

