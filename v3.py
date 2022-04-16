from selenium import webdriver
from datetime import datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time, os
##########
f=open("/sdcard/0ubuntu/sll.txt","r")
a=f.readline()
f.close()
os.system('clear')
n=0
#s=Service('/usr/bin/geckodriver')
while True:
  ##########
  if n==0 or n==99 or n==199:
    os.system('clear')
    mail='toaithanhha.hd@gmail.com'
  else:
    mail='dangnguyenthanhha3000'+str(a)+'@gmail.com'
  ##########
  try:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    driver = webdriver.Firefox(executable_path=('/usr/bin/geckodriver'), options=options)
    driver.get('https://limewire.com/invite/b806ce474046088f3e72')
  except TimeoutException:
    driver.quit()
    continue
  ##########
  try:
    myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section[2]/div[1]/form/div[1]/div[2]/input')))
    myElem.send_keys(mail)
    #print(".")
    time.sleep(2)
  except TimeoutException:
    driver.quit()
    continue
    print("nhu lon 1!")
  try:
    myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section[2]/div[1]/form/div[3]/button')))
    myElem.click()
    #print("..")
    time.sleep(2)
  except TimeoutException:
    driver.quit()
    continue
    print("nhu lon 2!")
  try:
    myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section[2]/div[2]/div[2]/div/div[2]/div')))
    #print("...")
    time.sleep(2)
  except TimeoutException:
    driver.quit()
    continue
    print("nhu lon 3!")
  ##########
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  try:
    num=driver.find_elements_by_css_selector(' .referral_info > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
    num1=driver.find_elements_by_css_selector('.referral_info > div:nth-child(1) > p:nth-child(2) > span:nth-child(2)')
    time.sleep(2)
  except:
    driver.quit()
    continue
    print("nhu lon 4!")
  for i in range(len(num)):
    print(n,a,num[i].text,num1[i].text,dt_string)
  ##########
  f=open("/sdcard/0ubuntu/sll.txt","w")
  f.write(str(a))
  f.close()
  a=int(a)+1
  n=n+1
  print("Wait a second!")
  time.sleep(5)
  driver.quit()
  ##########
