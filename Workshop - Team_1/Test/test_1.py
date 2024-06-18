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
    assert ({test_data.brand_name} in result for result in results), "No Lacoste sunglasses found"
    assert ({test_data.price_range} in result and float(result) for result in results), "Price filter not applied correctly"
    logging.info("Result information suit to searched data")