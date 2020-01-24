from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time


# establish a connection with chrome via my terminal
driver = webdriver.Chrome()

# go to greatschools.org
driver.get("https://www.greatschools.org/new-york/new-york/schools/?page=1")

# wait because the site is slow
# wait_loading = WebDriverWait(driver, 10)


while True:
    time.sleep(1) 
    ratings = driver.find_elements_by_xpath('//section[@class="school-list"]')
    for rating in ratings:
        
        rating_dict = {}

        try: 
            gs_rating = rating.find_element_by_xpath('//*[contains(@class, "circle-rating")]/text()').text
            print(gs_rating)
        except:
            continue

        # school_name = rating.find_element_by_xpath('')
        # school_address = rating.find_element_by_xpath('')
        # type_and_grades = rating.find_element_by_xpath('')
        # total_students = rating.find_element_by_xpath('')
    
        try: 
            next_page = driver.find_element_by_xpath('//*[contains(@class, "anchor-button   anchor-button")][last()]')
            next_page.click()

        # rating_dict['gs_rating'] = gs_rating
        # rating_dict['school_name'] = school_name
        # rating_dict['school_address'] = school_address
        # rating_dict['type_and_grades'] = type_and_grades
        # rating_dict['total_students'] = total_students

        except Exception as e:
            print(e)






            