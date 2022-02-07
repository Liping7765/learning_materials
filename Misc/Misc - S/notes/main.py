import os 
from selenium import webdriver

#re-set the path to locate the webdriver 
os.environ['PATH'] = r"C:/seleniumdriver"

#start the webdriver 
driver =  webdriver.Chrome()
driver.get("https://www.youtube.com/")

#implicit wait 
driver.implicitly_wait(8)

#locate element 
my_element = driver.find_element_by_id("video-title-link")

driver.find_element_by_css_selector(
    'a[aria-label]'
)

#execute action on the element 
my_element.click()
my_element.send_keys()

from selenium.webdriver.common.keys import Keys 
my_element.send_keys(Keys.ARROW_UP)

#close the browser 
driver.quit()



#explicit wait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"),#element 
        "complete"# expected text
    )
)