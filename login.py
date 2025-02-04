from selenium import webdriver
import pickle
import time

def save_cookies():
    driver = webdriver.Chrome()  
    driver.get("https://www.udemy.com/")  

    time.sleep(15)  # Wait for manual login

    pickle.dump(driver.get_cookies(), open("udemy_cookies.pkl", "wb"))
    driver.quit()
    print("Cookies saved successfully!")

save_cookies()