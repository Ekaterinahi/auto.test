import math, time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

element1 = browser.find_element_by_css_selector('#answer')
element1.send_keys(y)

browser.execute_script("window.scrollBy(0, 200);")

option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()

option2 = browser.find_element_by_css_selector("[type='submit']")
option2.click()


time.sleep(20)
browser.quit()