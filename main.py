from scraper import formatCar, saveCars, scrape, scrapeCar
from dotenv import load_dotenv
from selenium import webdriver
import os

load_dotenv()
try:
    vars={}
    vars['LINK_TO_SCRAPE'] = os.getenv('LINK_TO_SCRAPE')
    vars['MAX_BEFORE_SAVE'] = int(os.getenv('MAX_BEFORE_SAVE'))
    vars['MAX_TO_SCRAPE']=int(os.getenv('MAX_TO_SCRAPE'))
    vars['OUTPUT_FILE'] = os.getenv('OUTPUT_FILE')
    vars['CAR_DETAIL_COUNT'] = int(os.getenv('CAR_DETAIL_COUNT'))
    vars['ITEMS_IN_PAGE']=int(os.getenv('ITEMS_IN_PAGE'))
    
    driver = webdriver.Edge()
    scrape(driver,vars)
except:
    print('Something went wrong :(')
finally:
    driver.quit()