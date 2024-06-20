from Pages.product_page import ProductPage
import config
import logging
import test_data


def test_search_product(driver):
    product_page = ProductPage(driver)
    product_page.open_url(config.url)
    product_page.search_product(test_data.search_data)
    # Select brand and price range
    product_page.select_brand()
    product_page.select_price_range()
    results = product_page.get_results()
    logging.info(f"Geting search result {results}")
    logging.info("Checking search result suit to searched data")
    assert all(test_data.brand_name in result for result in results)
    "No Lacoste sunglasses found"
    logging.info(f"Brand: {test_data.brand_name} is in searched data: {results}")
    assert all(float(result.split("$")[1].split(" ")[0].strip('.')) <= float(
        test_data.price) for result in results)
    logging.info(f"Price: {test_data.price} is in searched data: {results}")
    logging.info("Result information suit to searched data")
    logging.info("Test passed")


# TODO
# 1. Locators in product_page.py is not effective, need to improve
# Thats good that you keep price and brand in test_data.py, but you could use that data in locators as well.
# e.g.: write brand and price locators In functions where you use them
"""
    def your_fucntion(self, brand_name, price):
        brand_name_filter = (By.XPATH, f"//ul[@aria-labelledby='brandNameFacet']//span[text()='{brand_name}']")
        brand_price_filter = (By.XPATH, f"//a[@class='uA-z']//span[text()='${price} and Under']")
        ....
        """
# And then in the test case you can call the function with the data from test_data.py
# I changed assert in test cases, the main issue was that you used assert without all() function 
# which is not correct because without all() functionthe expression inside the assertion will become a generator expression,
#  which is always True. So, I added all() function to the assert statements.
# I removed checking of price range in the result. Just checked that the price is less than 200.00 (will be better not hardcode price in the test)


