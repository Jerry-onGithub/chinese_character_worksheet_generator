# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:01:05 2022

@author: Jerry
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import csv
from webdriver_manager.firefox import GeckoDriverManager

link = 'https://www.purpleculture.net/chinese-practice-sheet/'

lesson = []
with open(r'C:/Users/.../Desktop/quizlet.csv' ) as h:   #change path to your local path where the file containing all chinese words and characters is located
    reader_obj = csv.reader(h, delimiter=',')
    rows = list(reader_obj)

    for i in range(len(rows)):
        try:
            if i>0:
                #add all characters/words in lesson
                lesson.append(rows[i][1])
        except:
            lesson.append("")
      
print(len(lesson))
print(len(rows))  

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:/Users/.../AppData/Local/Google/Chrome/User Data/Profile 1")   #change to profile path
driver = webdriver.Chrome(executable_path="C:/Users/.../Downloads/chromedriver_win32 (4)/chromedriver.exe", chrome_options=chrome_options)   #change to chromedriver path(version should be same with your browser version)

driver.get(link)
time.sleep(3)

driver.find_element_by_xpath("//a[@href='https://www.purpleculture.net/login/']").click()
time.sleep(3)

username = driver.find_element_by_id("login-email-address")
password = driver.find_element_by_id("login-password")

username.send_keys("...@gmail.com") #your account login email
time.sleep(1)
password.send_keys("...")   #account login password

login = driver.find_element_by_xpath("(//button[contains(@name, 'signin')])") 
login.click() 
newurl = driver.current_url
time.sleep(5)

check=[]
items=[]
count=20    #mine starts from lesson 20, you can adjust this to 1 or whatever you like
#for each character/word in lesson
for l in lesson:
    if count>0:
        title = "lesson " + str(count)
        if l != "":
          items.append(l)
        if l == "":
            print(len(items))
            check.append(len(items))
            listToStr = ' '.join([str(elem) for elem in items])
            
            ######
            input1 = driver.find_element_by_id("title")
            input2 = driver.find_element_by_id("sheet_content")
            
            input1.clear()
            input1.send_keys(title)
            time.sleep(1)
            input2.clear()
            input2.send_keys(listToStr)
            time.sleep(1)
            
            #you can adjust these according to your preferences
            style = Select(driver.find_element_by_id('grid_style'))
            style.select_by_index(5)
            size = Select(driver.find_element_by_id('grid_size'))
            size.select_by_index(0)
            phonetics = Select(driver.find_element_by_id('phonetics'))
            phonetics.select_by_index(1)
            traceable = Select(driver.find_element_by_id('traceable'))
            traceable.select_by_index(5)
            
            checkbox = driver.find_element_by_id("wenglish")
            if checkbox.is_selected():
                print("")
            else:
                checkbox.click()
            time.sleep(1)
            driver.find_element_by_id("checkvalue").click()
            time.sleep(3)
            
            items.clear()        
            count-=1
        

print("checks: ", ' '.join([str(elem) for elem in check]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
