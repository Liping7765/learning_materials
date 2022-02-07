import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#re-set the path to locate the webdriver 
os.environ['PATH'] = r"C:/seleniumdriver"

#start the webdriver 
driver =  webdriver.Chrome()
driver.get("https://www.remove.bg/upload")
driver.implicitly_wait(30)

button = driver.find_element_by_css_selector(
    'button[class="btn btn-primary btn-lg"]'
)

button.click()



upload = driver.find_element_by_name("image[original]")
upload.send_keys(r"C:\Users\Liping\Desktop\learning_materials\Misc\Misc - S\3-trans.png")

