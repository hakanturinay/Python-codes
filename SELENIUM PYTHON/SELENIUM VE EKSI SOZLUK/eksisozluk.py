from selenium import webdriver
import time
import random
browser = webdriver.Chrome("/Users/hakanturinay/Downloads/chromedriver")
url = "https://eksisozluk.com/yaran-inci-sozluk-entryleri--2269572?p="
pageCount = 1
entries = []
entryCount = 1
while pageCount <=10:
    randomPage = random.randint(1,232)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    pageCount += 1
with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+ ".\n" + entry + "\n")
        file.write("********************************\n")
        entryCount +=1
    
#browser.get(url)
#time.sleep(5)
"""elements = browser.find_elements_by_css_selector(".content")
for element in elements:
    print(element.text)"""
browser.close()
