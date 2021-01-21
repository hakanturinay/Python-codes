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
time.sleep(5)
searchName = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
searchName.send_keys("gunnesekin")
time.sleep(3)
ismail= browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div")
ismail.click()
time.sleep(2)
def first_picture(): 
    
    # finds the first picture  
    pic = browser.find_element_by_class_name("_9AhH0")    
    pic.click()   # clicks on the first picture
def like_pic(): 
    time.sleep(3) 
    like = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button') 
  
    # you can find the like button using class name too 
    time.sleep(2) 
    like.click()   # clicking the like button 
        
def next_picture(): 
    time.sleep(2) 
  
    # finds the button which gives the next picture 
    nex = browser.find_element_by_class_name("_65Bje")   
    time.sleep(2) 
    return nex
def continue_liking(): 
    while(True): 
        next_el = next_picture() 
  
        # if next button is there then 
        if next_el != False:   
  
            # click the next button 
            next_el.click()    
            time.sleep(2) 
  
            # like the picture 
            like_pic()     
            time.sleep(2)             
        else: 
            print("not found")  
            break
 
first_picture() 
like_pic()
continue_liking()
