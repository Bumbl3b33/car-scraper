import csv
import logging
import math
import os
from datetime import date

from selenium.webdriver.common.by import By

from ScrapeError import ScrapePageNotFound

def init(override_vars):
    vars={}
    vars['LINK_TO_SCRAPE'] = os.getenv('LINK_TO_SCRAPE')
    vars['PATH_SEARCH_TERMS'] = os.getenv('PATH_SEARCH_TERMS')
    vars['MAX_TO_SCRAPE']=override_vars['MAX_TO_SCRAPE']
    vars['CAR_DETAIL_COUNT'] = int(os.getenv('CAR_DETAIL_COUNT'))
    vars['ITEMS_PER_PAGE']=int(os.getenv('ITEMS_PER_PAGE'))
    return vars

def saveCars(cars, car_type):
    try:
        file = "./logs/" + str(date.today()) + "_" + car_type + ".txt"
        f = open(file, mode='a', encoding='utf-8')
        f.write(cars)
    except:
        raise
    finally:
        f.close()

def scrapeCar(driver, id, detail_count):
    car = []
    try:
        name = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(id) +  ']/h2').text
        car.append(name)
        for j in range(1,detail_count):
            try:
                detail = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(id) +  ']/div[2]/div['+ str(j) + ']').text 
                car.append(detail)
            except:
                car.append("N/A")
        return car
    except:
        raise ScrapePageNotFound(id)

def formatCar(car):
    return repr(car).removeprefix("[").removesuffix("]") + "," + "\n"

def loadPage(driver,link,search_term, page):
    if (int(page) == 1):
        driver.get(link + '/' + str(search_term)) 
    else:
        driver.get(link + '/' + str(search_term) + '?page=' + str(page)) 


def getSearchTerms(file_path):
    search_terms = []
    try:
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                search_terms.append(row[0].removesuffix(","))
    except:
        raise
    finally:
        csvfile.close()
        return search_terms

def scrapeTerm(driver,vars,search_term,pages):
    for page in range(1,pages):
        cars = ""
        try:
            loadPage(driver,vars['LINK_TO_SCRAPE'],search_term,page)
            cars = ""
            for i in range(1,vars['ITEMS_PER_PAGE']+1):
                car = scrapeCar(driver, i, vars['CAR_DETAIL_COUNT'])
                cars = cars + formatCar(car)
        except ScrapePageNotFound:
            logging.info("Page Not Found for Car Type:",search_term, "Car Number:",id)
            return
        except:
            raise
        finally:
            saveCars(cars,search_term)  

def scrape(driver,vars):
    try:
        pages = math.ceil(vars['MAX_TO_SCRAPE']/vars['ITEMS_PER_PAGE']) + 1
        terms = getSearchTerms(vars['PATH_SEARCH_TERMS'])
        for term in terms:
            scrapeTerm(driver, vars, term,pages)        
    except:
        raise  
