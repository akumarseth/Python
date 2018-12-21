from selenium import webdriver
from time import sleep
from getpass import getpass

usr=input('Enter Email Id:')
pwd = input('Enter Password:')
# pwd = getpass("Enter pssword: ")

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
