from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.support.wait import WebDriverWait
from threading import *

class WebScrapper:
    def GetReviews(url):
        #Setting up webdriver
        opt = ChromiumOptions()

        #No GUI so it runs faster
        opt.add_argument('--headless=new')
        #Helps Stop websites from detecting bot
        opt.add_argument(f"--user-agent={"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}")

        #Sets up webdriver and waits until Amazon is pulled up
        driver = webdriver.Chrome(options = opt)
        driver.get(url)
        wait = WebDriverWait(driver,timeout= 120)
        wait.until(lambda d: driver.find_element(By.ID,"twotabsearchtextbox").is_displayed())
        
        #Finds the reviews of items
        Reviews = driver.find_elements(By.CLASS_NAME,"review-text-content")

        #Prepares output file
        fileName = driver.find_element(By.ID, "productTitle").text + ".txt"
        file = open(fileName, "w+",encoding="utf-8")

        for Review in Reviews:
            #Writes reviews up to max review
            file.write(Review.text.strip() + "\n")
            file.write("-"+ "\n")

        #Closes the webdriver
        driver.close()
        driver.quit()
        file.close()
        return fileName
    