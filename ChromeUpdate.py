from selenium import webdriver
import time
driver = webdriver.Chrome("D:\\BOTIK\\mashBot\\mashBot\\proj\\bot\\chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=o_QH9Zdl4R8")
time.sleep(5)
driver.close()