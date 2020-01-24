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

csv_file = open('great_schools.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
# wait because the site is slow
# wait_loading = WebDriverWait(driver, 10)

# EVERYTHING ABOVE IS WORKING!
index = 1
while index < 46:
    try:
        print("Scraping Page number " + str(index))
        index += 1
       
        wait_rating = WebDriverWait(driver, 30)
        ratings = wait_rating.until(EC.presence_of_all_elements_located((By.XPATH,'//section[@class="school-list"]')))

        # time.sleep(10) 
        # ratings = driver.find_elements_by_xpath('//section[@class="school-list"]')
        
        for rating in ratings:
            
            rating_dict = {}

            try: 
                gs_rating = rating.find_element_by_xpath('.//*[contains(@class, "circle-rating")]').text
                print(gs_rating)
            except:
                continue
            
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
            except:
                continue   
            
            rating_dict['gs_rating'] = gs_rating
            rating_dict['school_name'] = school_name
            rating_dict['school_address'] = school_address
            rating_dict['type_and_grades'] = type_and_grades
            rating_dict['total_students'] = total_students

            writer.writerow(rating_dict.values())

        next_page = driver.find_element_by_xpath('//*[contains(@class, "anchor-button   anchor-button")][last()]')
        next_page.click()

    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break

