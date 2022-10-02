from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
try:
    LINK_TO_SCRAPE = os.getenv('LINK_TO_SCRAPE')
    SCRAPE_COUNT = int(os.getenv('SCRAPE_COUNT'))
    OUTPUT_FILE = os.getenv('OUTPUT_FILE')
    CAR_DETAIL_COUNT = int(os.getenv('CAR_DETAIL_COUNT'))
except:
    raise ValueError("Failed to load env variables")

driver = webdriver.Edge()
driver.get(LINK_TO_SCRAPE + '/axio')

cars = ""
for i in range(1,SCRAPE_COUNT):
        
    car = []
    name = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(i) +  ']/h2').text
    car.append(name)
    for j in range(1,CAR_DETAIL_COUNT):
        detail = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(i) +  ']/div[2]/div['+ str(j) + ']').text 
        car.append(detail)
    
    car_as_csv = repr(car).removeprefix("[").removesuffix("]") + "," + "\n"
    cars = cars + car_as_csv

try:
    f = open(OUTPUT_FILE, mode='a', encoding='utf-8')
    f.write(cars)
finally:
    f.close()

driver.quit()