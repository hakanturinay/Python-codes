from selenium import webdriver
import time
browser = webdriver.Chrome("/Users/hakanturinay/Downloads/chromedriver")
browser.get("https://www.instagram.com/")
time.sleep(1)


username  = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password  = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
username.send_keys("hakanturinay")
password.send_keys("253860tr")
time.sleep(1)

login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]")
login.click()
time.sleep(2)

profilebutton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
profilebutton.click()
time.sleep(2)

buttons = browser.find_elements_by_css_selector(".Y8-fY ")
folllowersButton = buttons[1]
folllowersButton.click()
time.sleep(5)

jscommand = """
    followers = document.querySelector(".isgrP");
    followers.scrollTo(0,followers.scrollHeight);
    var lenOfPage=followers.body.scrollHeight;
    return lenOfP;
"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
browser.close()
