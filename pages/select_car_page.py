import logging

import allure
from locators.locators import SelectCarLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from selenium.webdriver.common.action_chains import ActionChains


class SelectCarPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 20, poll_frequency=5)

    @allure.step("Opening Pod point checkout website")
    def open_url(self):
        self.logger.info("Opening Pod point checkout website")
        self.driver.get("https://checkout.pod-point.com/")

    @allure.step("Selecting car make and model")
    def select_car(self):
        self.logger.info("Selecting car make and model")
        self.wait.until(EC.element_to_be_clickable((By.ID, SelectCarLocators.car_make_dd)))
        car_model_dd = Select(self.driver.find_element(By.ID, SelectCarLocators.car_make_dd))
        car_model_dd.select_by_visible_text('Mitsubishi')
        self.wait.until(EC.element_to_be_clickable((By.ID, SelectCarLocators.model_car_dd)))
        car_type_dd = Select(self.driver.find_element(By.ID, SelectCarLocators.model_car_dd))
        car_type_dd.select_by_visible_text('Outlander')

        self.wait.until(EC.presence_of_element_located((By.NAME, "dealershipDiscount")))
        self.wait.until(EC.presence_of_element_located((By.ID, SelectCarLocators.dealer_discount_cb)))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        obj = self.wait.until(EC.presence_of_element_located((By.ID, SelectCarLocators.dealer_discount_cb)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", obj)

        self.driver.find_element(By.ID, SelectCarLocators.dealer_discount_cb).click()

    @allure.step("selecting connection types")
    def select_connection(self):
        self.logger.info("selecting connection types")
        self.wait.until(EC.presence_of_element_located((By.ID, SelectCarLocators.conn_type_rb)))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        obj = self.wait.until(EC.presence_of_element_located((By.ID, SelectCarLocators.conn_type_rb)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", obj)

        self.driver.find_element(By.XPATH, SelectCarLocators.conn_type_label).click()

    @allure.step("selecting power rating 7kw")
    def select_power_rating(self):
        self.logger.info("selecting power rating 7kw")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        obj = self.wait.until(EC.presence_of_element_located((By.XPATH, SelectCarLocators.power_rating_kw7_label)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", obj)
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, SelectCarLocators.power_rating_kw7_label)
        action.move_to_element(element).click(element).perform()
        self.driver.find_element(By.XPATH, SelectCarLocators.power_rating_kw7_label).click()
        full_price = self.driver.find_element(By.XPATH, SelectCarLocators.kw7_full_price).text
        olev_price = self.driver.find_element(By.XPATH, SelectCarLocators.kw7_olev_price).text
        assert full_price == '£879.00'
        assert olev_price == '£529.00'

        return int(''.join(e for e in full_price if e.isalnum()))

    @allure.step("selecting extra features")
    def select_compatible_extra(self):
        self.logger.info("selecting extra feature")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.wait.until(EC.presence_of_element_located((By.ID, SelectCarLocators.power_rating_kw7)))
        obj = self.wait.until(EC.presence_of_element_located((By.XPATH, SelectCarLocators.comp_extra_list)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", obj)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, SelectCarLocators.comp_extra_list)))
        comp_list = self.driver.find_elements(By.XPATH, SelectCarLocators.comp_extra_list)
        price_list = self.driver.find_elements(By.XPATH, SelectCarLocators.comp_price_list)
        i = random.randint(0, len(comp_list) - 1)
        obj = self.wait.until(EC.presence_of_element_located((By.ID, SelectCarLocators.next_btn)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", obj)
        comp_list[i].click()
        comp_price = price_list[i].text
        return int(''.join(e for e in comp_price if e.isalnum()))

    @allure.step("checking final price is correct")
    def verify_final_price(self, base_price, extra_price):
        self.logger.info("checking final price is correct")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, SelectCarLocators.comp_extra_list)))
        total_price = base_price + extra_price
        self.wait.until(EC.invisibility_of_element((By.XPATH, SelectCarLocators.next_loading_btn)))
        ui_price = self.driver.find_element(By.XPATH, SelectCarLocators.final_price).text
        final_price = int(''.join(e for e in ui_price if e.isalnum()))
        assert total_price == final_price, "test failed because total price" + str(total_price) + "is not equal to" \
                                                                                                  " final_price=" + str(
            final_price)

    @allure.step("accept cookies")
    def accept_cookies(self):
        self.logger.info("accepting cookies")
        self.driver.find_element(By.XPATH, SelectCarLocators.close_pop_header).click()
        self.driver.find_element(By.CLASS_NAME, SelectCarLocators.cookie_btn_class).click()
