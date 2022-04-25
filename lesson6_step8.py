from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_tag_name(".form-control.first")
    input1.send_keys("Kate")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    input2 = browser.find_element_by_class_name("form-control.second")
    input2.send_keys("Kozina")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("Ekt@nlj.km")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click() 

    time.sleep(25)

    welcome_text_elt = browser.find_element_by_tag_name("div")

    welcome_text = welcome_text_elt.text

   
    assert "NoSuchElementException" == welcome_text

finally:

    time.sleep(20)

    browser.quit()
