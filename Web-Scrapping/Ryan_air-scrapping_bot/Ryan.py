# Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd
import os

# static data
x = ['Bratislava', 'Vienna', 'Budapest']
destination = "Any destination"
months =  ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
no_of_days = [2,3,4,5,6,7]
name_of_days =  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def ryan_air_scraping():
    print("******* Ryan Air Scrapping *****")

    # to store the data
    data = []

    driver = webdriver.Chrome()
    driver.get("https://www.ryanair.com/")

    # cookies
    wait = WebDriverWait(driver, 10)
    cookie_popup = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cookie-popup-with-overlay__button")))
    cookie_popup.click()

    time.sleep(1)
    print("Data Loading",end=" ")
    for origin_city in x:
        for month in months:
            for num_of_days in range(0, len(no_of_days)):
                for day_name in name_of_days:
                    print(".",end=" ")
                    origin = driver.find_element(By.ID, "input-button__departure")
                    origin.click()
                    origin.clear()
                    time.sleep(1)
                    origin.send_keys(origin_city)

                    time.sleep(.5)
                    destination = driver.find_element(By.ID, 'input-button__destination')
                    destination.click()

                    time.sleep(2)  # Wait for 2 seconds

                    span_element = driver.find_element(By.XPATH, "//span[contains(text(), 'Any destination')]")
                    span_element.click()

                    # date
                    date_div = driver.find_element(By.XPATH, "//div[contains(text(), 'Choose date')]")
                    # date
                    time.sleep(2)
                    # selecting_flexible_date = driver.find_element(By.XPATH, "//span[contains(text(), 'Flexible dates')]").click()
                    selecting_flexible_date = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Flexible dates')]")))

                    time.sleep(1)
                    if (month == "Dec"):
                        click_arrow = driver.find_element(By.CSS_SELECTOR,
                                                          "span._container.icon-18.icon-light-blue svg").click()
                        time.sleep(0.5)
                        selecting_month = driver.find_element(By.XPATH,
                                                              f"//fsw-element-item[contains(text(), '{month}')]").click()

                    else:
                        selecting_month = driver.find_element(By.XPATH,
                                                              f"//fsw-element-item[contains(text(), '{month}')]").click()

                    # side bar for days
                    slider_bar_thumb = driver.find_element(By.CLASS_NAME, "slider__thumb")
                    ActionChains(driver).drag_and_drop_by_offset(slider_bar_thumb, 15 * num_of_days, 0).perform()

                    # selecting the day name
                    selcting_day = driver.find_element(By.XPATH,
                                                       f"//fsw-element-item[contains(text(), '{day_name}')]").click()

                    # apply btn
                    time.sleep(1)
                    apply_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()

                    search_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Search')]").click()
                    time.sleep(8)

                    try:
                        fligt_div = driver.find_element(By.CLASS_NAME, "ng-star-inserted")


                        country_name = driver.find_elements(By.CSS_SELECTOR, 'h2.country-card__country')
                        try:
                            button = driver.find_elements(By.CSS_SELECTOR, "span[class*='place-card__icon']")
                        except:
                            print('Button error')

                        if (len(country_name) <= 1):
                            print('he')
                            time.sleep(5)
                            cities = driver.find_elements(By.CSS_SELECTOR, "h2.cities__city.h4")
                            fares = driver.find_elements(By.CSS_SELECTOR, 'span.cities__price.h4')

                            city_list = []
                            fare_list = []

                            for k in range(len(cities)):
                                city = cities[k].text
                                fare = fares[k].text
                                if city != '':
                                    city_list.append(city)
                                    fare_list.append(fare)

                            data.append({'Origin Country': origin_city, 'Destination-Country': country,
                                         'Destination-Cities': city_list, 'Fare': fare_list})
                            """
                            for city, fare in zip(city_list, fare_list):
                                print("City:", city)
                                print("Fare:", fare)
                                print("origin_city", origin_city) """
                            time.sleep(2)
                        else:
                            try:
                                view_more_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//button[contains(text(), 'View more destinations')]")))
                                view_more_button.click()
                                # scroll back up for getting results from start
                                driver.execute_script("window.scrollTo(0, 0)")

                                # getting again the country name and button
                                time.sleep(1)
                                country_name = driver.find_elements(By.CSS_SELECTOR, 'h2.country-card__country')
                                time.sleep(1)
                                button = driver.find_elements(By.CSS_SELECTOR, "span[class*='place-card__icon']")
                                for i in range(len(country_name)):
                                    country = country_name[i].text
                                    #print("Country -->",country)
                                    time.sleep(2)
                                    a = ActionChains(driver)
                                    a.move_to_element(button[i]).click().perform()
                                    #print("Down btn clicked")
                                    time.sleep(5)
                                    cities = driver.find_elements(By.CSS_SELECTOR, "h2.cities__city.h4")
                                    fares = driver.find_elements(By.CSS_SELECTOR, 'span.cities__price.h4')

                                    city_list = []
                                    fare_list = []

                                    for k in range(len(cities)):
                                        city = cities[k].text
                                        fare = fares[k].text
                                        if city != '':
                                            city_list.append(city)
                                            fare_list.append(fare)

                                    data.append({'Origin Country': origin_city, 'Destination-Country': country,
                                                 'Destination-Cities': city_list, 'Fare': fare_list})

                                    """for city, fare in zip(city_list, fare_list):
                                        print("City:", city)
                                        print("Fare:", fare)
                                        print("origin_city", origin_city)
                                    """

                            except (NoSuchElementException,TimeoutException):
                                for i in range(len(country_name)):
                                    country = country_name[i].text
                                    #print("Country:", country)
                                    time.sleep(2)
                                    a = ActionChains(driver)
                                    a.move_to_element(button[i]).click().perform()
                                    time.sleep(5)
                                    cities = driver.find_elements(By.CSS_SELECTOR, "h2.cities__city.h4")
                                    fares = driver.find_elements(By.CSS_SELECTOR, 'span.cities__price.h4')

                                    city_list = []
                                    fare_list = []

                                    for k in range(len(cities)):
                                        city = cities[k].text
                                        fare = fares[k].text
                                        if city != '':
                                            city_list.append(city)
                                            fare_list.append(fare)

                                    data.append({'Origin Country': origin_city, 'Destination-Country': country,
                                                 'Destination-Cities': city_list, 'Fare': fare_list})
                                    """
                                    for city, fare in zip(city_list, fare_list):
                                        print("City:", city)
                                        print("Fare:", fare)
                                        print("origin_city", origin_city)
"""
                            time.sleep(2)
                        driver.back()
                        time.sleep(5)
                    except NoSuchElementException:
                        print('NoSuchElementException')

        # origin loop ends

    # after that closing the browser
    time.sleep(1)

    # making data frame
    df = pd.DataFrame(data)
    print("\n")
    print(df)

    # checking if the csv file exist or not
    file = "Ryanair.csv" # you can change the file name here
    if (os.path.exists(file)):
        print("File Exist")
        df.to_csv(file, mode='a', header=False, index=False, encoding="utf-8-sig")
    else:
        df.to_csv(file, encoding='utf-8-sig', index=False)


    driver.close()
    print("******* Scrapping Completed and Data is Stored in "+file+" *************")





# To Run the code  just click here
if __name__ == '__main__':
    ryan_air_scraping()

