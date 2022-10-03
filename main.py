import logging
import os

from dotenv import load_dotenv
from selenium import webdriver

from scraper import scrape

load_dotenv()

"""
USER-CONFIGURABLE
"""
MAX_TO_SCRAPE = 400

try:
    vars={}
    vars['LINK_TO_SCRAPE'] = os.getenv('LINK_TO_SCRAPE')
    vars['MAX_TO_SCRAPE']=MAX_TO_SCRAPE
    vars['OUTPUT_FILE'] = os.getenv('OUTPUT_FILE')
    vars['CAR_DETAIL_COUNT'] = int(os.getenv('CAR_DETAIL_COUNT'))
    vars['ITEMS_PER_PAGE']=int(os.getenv('ITEMS_PER_PAGE'))

    driver = webdriver.Edge()
    scrape(driver,vars)
except BaseException:
    logging.exception("An exception was thrown!")
finally:
    driver.quit()
