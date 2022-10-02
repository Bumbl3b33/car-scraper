from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
try:
    LINK_TO_SCRAPE = os.getenv('LINK_TO_SCRAPE')
    SCRAPE_COUNT = int(os.getenv('SCRAPE_COUNT'))
    OUTPUT_FILE = os.getenv('OUTPUT_FILE')
except:
    raise ValueError("Failed to load env variables")

driver = webdriver.Edge()
driver.get(LINK_TO_SCRAPE + '/axio')

for i in range(1,SCRAPE_COUNT):
        
    car = []
    name = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(i) +  ']/h2').text
    car.append(name)
    for j in range(1,5):
        detail = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(i) +  ']/div[2]/div['+ str(j) + ']').text 
        car.append(detail)

    try:
        f = open("cars.txt", mode='a', encoding='utf-8')
        car_as_csv = repr(car).removeprefix("[").removesuffix("]") + "," + "\n"
        f.write(car_as_csv)
    finally:
        f.close()

driver.quit()
