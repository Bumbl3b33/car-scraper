from datetime import date
from logging import exception
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
        detail = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[' + str(id) +  ']/div[2]/div['+ str(j) + ']').text 
        car.append(detail)
    return car

def formatCar(car):
    return repr(car).removeprefix("[").removesuffix("]") + "," + "\n"

def scrape(driver,vars):
    try:
        driver.get(vars['LINK_TO_SCRAPE'] + '/axio')
        cars = ""
        for i in range(1,vars['MAX_TO_SCRAPE']):
                try:
                    if (i % vars['MAX_BEFORE_SAVE'] == 0):
                        saveCars(cars)
                        cars = ""
                    
                    car = scrapeCar(driver, i, vars['CAR_DETAIL_COUNT'])
                    cars = cars + formatCar(car)
                except:
                    raise
                finally:
                    saveCars(cars)  
                    cars = ""
    except:
        raise  