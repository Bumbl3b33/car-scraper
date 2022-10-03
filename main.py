import logging

from dotenv import load_dotenv
from selenium import webdriver

from scraper import init, scrape

load_dotenv()

"""
USER-CONFIGURABLE
"""
MAX_TO_SCRAPE = 400

try:
    config = init({'MAX_TO_SCRAPE':MAX_TO_SCRAPE})
    driver = webdriver.Edge()
    scrape(driver,config)
except BaseException:
    logging.exception("An exception was thrown!")
finally:
    driver.quit()
