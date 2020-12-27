import pytest
from pages.select_car_page import SelectCarPage


@pytest.mark.usefixtures("setup")
class TestSelectCar:
    def test_check_car_purchase(self):
        select_car_page = SelectCarPage(self.driver)

        select_car_page.open_url()
        select_car_page.accept_cookies()
        select_car_page.select_car()

        select_car_page.select_connection()
        price1 = select_car_page.select_power_rating()
        extra_price = select_car_page.select_compatible_extra()
        select_car_page.verify_final_price(price1, extra_price)
