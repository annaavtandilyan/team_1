from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import test_data


class ProductPage(BasicHelper):
    search_input_loc = (By.XPATH, "//input[@placeholder='Search 6pm.com']")
    btn_search_loc = (By.XPATH, "//button[@type='submit']")
    search_result_loc = (By.XPATH, "//a[@class='fo-z']")
    brand_filter_loc = (By.XPATH, "//aside[@id='searchFilters']/div[1]/div[2]/section[3]/div[2]/ul[1]/li[3]/a[1]")
    scroll_loc = (By.XPATH, '//button[@data-selected-facet-group-name="colorFacet"]')
    price_filter_loc = (By.XPATH, "//aside[@id='searchFilters']/div[1]/div[2]/section[4]/div[1]/ul[1]/li[1]/a[1]")
   
    def search_product(self, product_name):
        self.find_and_send_keys(self.search_input_loc, product_name)
        self.find_and_click(self.btn_search_loc)
        logging.info(f"Searching for product: {product_name}")

    def select_brand(self):
        self.find_and_click(self.brand_filter_loc)
        logging.info(f"Selected brand: {test_data.brand_name}")

    def select_price_range(self):
        time.sleep(2)
        logging.info("Scrolled to find 'Price' checkbox")
        scroll = self.find_elem_ui(self.scroll_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll).perform()
        self.find_and_click(self.price_filter_loc)
        logging.info(f"Selected price range: {test_data.price_range}")

    def get_results(self):
        search_result = self.find_elements(self.search_result_loc)
        return [item.text for item in search_result]
    
