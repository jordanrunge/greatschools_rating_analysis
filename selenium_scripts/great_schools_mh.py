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

csv_file = open('great_schools_mh.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
# wait because the site is slow
# wait_loading = WebDriverWait(driver, 10)

# EVERYTHING ABOVE IS WORKING!
index = 1
while index < 46:
    try:
        print('\n')
        print("Scraping Page number " + str(index))
        print("+"*88)
        index += 1
       
        wait_rating = WebDriverWait(driver, 30)
        ratings = wait_rating.until(EC.presence_of_all_elements_located((By.XPATH,'//ol/li[@class=" unsaved"]')))
        # ratings = wait_rating.until(EC.presence_of_all_elements_located((By.XPATH,'//section[@class="school-list"]')))

        # time.sleep(10) 
        # ratings = driver.find_elements_by_xpath('//section[@class="school-list"]')
        
        for rating in ratings:
            
            rating_dict = {}

            try: 
                gs_rating = rating.find_element_by_xpath('.//*[contains(@class, "circle-rating")]').text
                print(gs_rating)
            except:
                gs_rating = rating.find_element_by_xpath('.//*[contains(@alt, "Owl ")]').text
                print(gs_rating)
            
            try:
                school_name = rating.find_element_by_xpath('.//a[@class="name"]').text
                print(school_name)
            except:
                continue

            try:
                school_address = rating.find_element_by_xpath('.//div[@class="address"]').text
                print(school_address)
            except:
                continue

            try:
                type_and_grades = rating.find_element_by_xpath('.//div/span[@class="open-sans_sb"]').text
                print(type_and_grades)
            except:
                continue

            try:
                total_students = rating.find_element_by_xpath('.//span/span[@class="open-sans_sb"]').text
                print(total_students)
                print("-"*12)
            except:
                continue   
            
            rating_dict['gs_rating'] = gs_rating
            rating_dict['school_name'] = school_name
            rating_dict['school_address'] = school_address
            rating_dict['type_and_grades'] = type_and_grades
            rating_dict['total_students'] = total_students

            writer.writerow(rating_dict.values())

         # We need to scroll to the bottom of the page because the button is not in the current view yet.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        wait_next = WebDriverWait(driver, 10)
        next_page = wait_next.until(EC.element_to_be_clickable((By.XPATH,'//*[contains(@class, "anchor-button   anchor-button")][last()]')))
        next_page.click()
        time.sleep(1)

    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break

