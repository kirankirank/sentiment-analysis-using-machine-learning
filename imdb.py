import time
from webbrowser import Chrome

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# driver = Firefox(service =Service(GeckoDriverManager().install()))
driver = webdriver.Chrome(executable_path="D:\\SeleniumPython\\Browsers\\chromedriver.exe")
driver.get("https://www.imdb.com/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID, "suggestion-search").send_keys("KGF 2")
driver.find_element(By.ID, "suggestion-search-button").click()
driver.find_element(By.LINK_TEXT, 'K.G.F: Chapter 2').click()
driver.find_element(By.LINK_TEXT, "User reviews").click()
# review = driver.find_element(By.XPATH,"//div[contains(@class,'imdb-u]ser-review')]")
for i in range(1, 77):
    # driver.find_element(By.XPATH, "//button[@class='ipl-load-more__button']").click()
    driver.find_element(By.XPATH, "//div[@class='ipl-load-more ipl-load-more--loaded'] //button").click()
all_ok = driver.find_elements(By.CLASS_NAME, "lister-item-content")
Rating = []
Title = []
Review = []
Name_Date = []
for i in all_ok:
    sen = i.text
    print(sen)
    sen = sen.split("\n")
    Rating.append(sen[0])
    Title.append(sen[1])
    Name_Date.append(sen[2])
    Review.append(sen[3])

print(len(Name_Date), len(Title), len(Review), len(Rating))
kiran = pd.DataFrame({"name": Name_Date, "Title": Title, "comment": Review, "rating": Rating})
kiran.to_csv("kiran.csv")

