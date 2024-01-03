import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service(r"D:\python\django-chat\chromedriver.exe")

driver = webdriver.Chrome(service=s)
    
driver.get('http://localhost:8000/login/');

time.sleep(3) 

username_box = driver.find_element(by=By.ID,value= "id_username")
password_box = driver.find_element(by=By.ID,value= "id_password")

username_box.send_keys('hafiz')
password_box.send_keys('123456')

login_btn = driver.find_element(by=By.ID, value="loginBtn")
login_btn.click()

time.sleep(3) 

driver.get('http://localhost:8000/chat/haseeb');

time.sleep(3) 


msg_box = driver.find_element(by=By.ID,value= "msg_field")
msg_btn = driver.find_element(by=By.ID,value= "send_btn")
msg_box.send_keys('Hello!')

msg_btn.click()

time.sleep(5) 

driver.quit()