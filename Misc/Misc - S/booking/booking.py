from lib2to3.pgen2 import driver
import booking.constants as const 
import os 
from selenium import webdriver

class Booking(webdriver.Chrome):

    def __init__(self, driver_path = r"C:/seleniumdriver", teardown = False ):
        os.environ["PATH"] = driver_path
        self.teardown = teardown 
        super().__init__()
        self.implicitly_wait(15)

    def land_the_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def get_vedio_info(self):

        titles = self.find_elements_by_id("video-title")
        links = self.find_elements_by_id("video-title-link")
        result = {}

        for index in range(len(titles)):
            result[titles[index].get_attribute("innerHTML").strip()] = links[index].get_attribute('href')
