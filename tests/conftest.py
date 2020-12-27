import os, os.path
import pytest
from allure_commons.types import AttachmentType
import allure
from utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    mypath = "/reports"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
