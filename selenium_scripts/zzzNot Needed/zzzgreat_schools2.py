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

index = 1
while index is True:
    try:
        print('Scrapping page number ' + str(index))
        index = index + 1
        wait_review = WebDriverWait(driver, 10) 
        ratings = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//section[@class="school-list"]')))
        
        for rating in ratings:
            
            rating_dict = {}
            
            try: 
                gsrating = rating.find_element_by_xpath('//*[contains(@class, "circle-rating")]').text
                print(rating)
            except Exception as e:
                continue


        
        next_page_exists = False
        try: 
            next_page = driver.find_element_by_xpath('//*[contains(@class, "anchor-button   anchor-button")][last()]')
            next_page.click()
            next_page_exists = True
            time.sleep(.5)
        except:
            break 













next_button = driver.find_element_by_xpath('//*[contains(@class, "icon-chevron-right")]').click()

/new-york/new-york/schools/?page=3
/new-york/new-york/schools/?page=3
/new-york/new-york/schools/?page=3
/new-york/new-york/schools/?page=3






csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
while True:
    try:
        print("Scraping Page number " + str(index))
        index = index + 1
        # Find all the reviews on the page
        wait_review = WebDriverWait(driver, 10)
        reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
                                    '//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')))
        for review in reviews:
            # Initialize an empty dictionary for each review
            review_dict = {}
            # Use relative xpath to locate the title, text, username, date, rating.
            # Once you locate the element, you can use 'element.text' to return its string.
            # To get the attribute instead of the text of each element, use 'element.get_attribute()'
            try:
                title = review.find_element_by_xpath('.//div[@class="NHaasDS75Bd fontSize_12 wrapText"]').text
            except:
                continue

            # OPTIONAL PART 1a
            # Attempts to click the "read more" button to expand the text. This needs to be clicked
            # a second time otherwise the button click in the next review will collapse the previous
            # review text (and won't expand the current text).

            # We also need to scroll to the review element first because the button is not in the current view yet.
            driver.execute_script("arguments[0].scrollIntoView();", review)

            read_more_exists = False
            try:
                read_more = review.find_element_by_xpath('.//a[@class="border_gray onlyBottomBorder color_000 fontSize_1"]')
                read_more.click()
                read_more_exists = True
                # Slows down the text expansion so the text can be scraped
                time.sleep(.5)
            except:
                pass

            text = review.find_element_by_xpath('.//span[@class="pad6 onlyRightPad"]').text
            username = review.find_element_by_xpath('.//span[@class="padLeft6 NHaasDS55Rg fontSize_12 pad3 noBottomPad padTop2"]').text
            date_published = review.find_element_by_xpath('.//span[@class="NHaasDS55Rg fontSize_12  pad3 noBottomPad padTop2"]').text
            rating = review.find_element_by_xpath('.//span[@class="positionAbsolute top0 left0 overflowHidden color_000"]').get_attribute('style')
            rating = int(re.findall('\d+', rating)[0])/20

            # OPTIONAL PART 1b
            # Click the read more button if it exists in order to collapse the text for the current review
            if read_more_exists:
                read_more.click()

            review_dict['title'] = title
            review_dict['text'] = text
            review_dict['username'] = username
            review_dict['date_published'] = date_published
            review_dict['rating'] = rating

            writer.writerow(review_dict.values())

        # We need to scroll to the bottom of the page because the button is not in the current view yet.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Locate the next button on the page.
        wait_button = WebDriverWait(driver, 10)
        next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
                                    '//li[@class="nextClick displayInlineBlock padLeft5 "]')))
        next_button.click()
    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break