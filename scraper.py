from datetime import date
import math
from selenium.webdriver.common.by import By

def saveCars(cars):
    try:
        file_name = str(date.today())
        file = "./logs/" + file_name + ".txt"
        f = open(file, mode='a', encoding='utf-8')
        f.write(cars)
    except:
        raise
    finally:
        f.close()

def scrapeCar(driver, id, detail_count):
    car = []
    name = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(id) +  ']/h2').text
    car.append(name)
    for j in range(1,detail_count):
        try:
            detail = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(id) +  ']/div[2]/div['+ str(j) + ']').text 
            car.append(detail)
        except:
            car.append("N/A")
    return car

def formatCar(car):
    return repr(car).removeprefix("[").removesuffix("]") + "," + "\n"

def loadPage(driver,link, page):
    if (int(page) == 1):
        driver.get(link + '/axio') 
    else:
        driver.get(link + '/axio' + '?page=' + str(page)) 

def scrape(driver,vars):
    try:
        target_pages = math.ceil(vars['MAX_TO_SCRAPE']/vars['ITEMS_PER_PAGE']) + 1
        
        for page in range(1,target_pages):
            cars = ""
            try:
                loadPage(driver,vars['LINK_TO_SCRAPE'],page)
                cars = ""
                for i in range(1,vars['ITEMS_PER_PAGE']+1):
                    car = scrapeCar(driver, i, vars['CAR_DETAIL_COUNT'])
                    cars = cars + formatCar(car)
            except:
                raise
            finally:
                saveCars(cars)  
    except:
        raise  