from Helpers.basic_page import BasicHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import test_data


class ProductPage(BasicHelper):
    search_input_loc = (By.XPATH, "//input[@placeholder='Search 6pm.com']")
    btn_search_loc = (By.XPATH, "//button[@type='submit']")
    search_result_loc = (By.XPATH, "//a[@class='Bn-z']")
    brand_filter_loc = (By.XPATH, f"//ul[@aria-labelledby='brandNameFacet']//span[text()='{test_data.brand_name}']")
    scroll_loc = (By.XPATH, '//button[@data-selected-facet-group-name="colorFacet"]')
    brand_price_filter = (By.XPATH, f"//a[@class='uA-z']//span[text()='${test_data.price} and Under']")
   
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
        self.find_and_click(self.brand_price_filter)
        logging.info(f"Selected price: {test_data.price}")

    def get_results(self):
        search_result = self.find_elements(self.search_result_loc)
        return [item.text for item in search_result]
