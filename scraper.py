from selenium.webdriver.common.by import By

def saveCars(output_file, cars):
    try:
        f = open(output_file, mode='a', encoding='utf-8')
        f.write(cars)
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