from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("/Users/hakanturinay/Downloads/chromedriver")
browser.get("https://www.twitter.com")
time.sleep(3)
giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div/div")
giris_yap.click()
time.sleep(2)

username  = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
password  = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
username.send_keys("hkntrny")
password.send_keys("253860rew")
time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span")
login.click()
time.sleep(2)

search_area = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div")
search_area.find_element_by_name("greenday").send_keys(Keys.ENTER)

time.sleep(3)


browser.close()
