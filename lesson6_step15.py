from xml.dom.minidom import Element
from selenium import webdriver
import time, os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_tag_name(".form-control")
    input1.send_keys("Kate")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Kozina")
    
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Ekt@nlj.km")
   
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson6_step15.txt')
    file_btn = browser.find_element_by_id("file")
    file_btn.send_keys(file_path)

    button2 = browser.find_element_by_class_name("btn")
    button2.click()
    assert True
   
finally:

    time.sleep(30)

    browser.quit()
