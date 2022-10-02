from scraper import formatCar, saveCars, scrapeCar
from dotenv import load_dotenv
from selenium import webdriver
import os

load_dotenv()
try:
    LINK_TO_SCRAPE = os.getenv('LINK_TO_SCRAPE')
    MAX_BEFORE_SAVE = int(os.getenv('MAX_BEFORE_SAVE'))
    MAX_TO_SCRAPE=int(os.getenv('MAX_TO_SCRAPE'))
    OUTPUT_FILE = os.getenv('OUTPUT_FILE')
    CAR_DETAIL_COUNT = int(os.getenv('CAR_DETAIL_COUNT'))
    ITEMS_IN_PAGE=int(os.getenv('ITEMS_IN_PAGE'))
except:
    raise ValueError("Failed to load env variables")

driver = webdriver.Edge()
driver.get(LINK_TO_SCRAPE + '/axio')

cars = ""
for i in range(1,MAX_TO_SCRAPE):

    # if(i % ITEMS_IN_PAGE == 0):
    #     driver.get( LINK_TO_SCRAPE + '/axio' + '?page=' + page_number)
    
    if (i % MAX_BEFORE_SAVE == 0):
        saveCars(OUTPUT_FILE,cars)
        cars = ""

    car = scrapeCar(driver, i, CAR_DETAIL_COUNT)
    cars = cars + formatCar(car)



driver.quit()