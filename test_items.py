from selenium import webdriver
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_check_if_add_button_found(browser):
    
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), 'ADD button is abscent!'

 




 

