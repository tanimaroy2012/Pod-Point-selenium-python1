# Pod point test automation project

The following project has the end to end flow for checking out from pod-point with a car purchase
and verify the correct checkout price is visible.

## Project Structure
Here you can find a short description of main directories and it's content
- [locators](locators) - there are locators of web elements in locators.py grouped in classes
- [pages](pages) - there are sets of method for each test step.
- [tests](tests) - there are sets of tests for main functionality of website
- [reports](reports) - if you run tests with Allure, tests reports will be saved in this directory
- [utils](utils) - this directory contains files responsible for configuration, e.g. driver_factory.py for webdriver management.

## Project Features
- framework follows page object pattern
- logger has been implemented in each step of test cases, e.g.

![Logs screenshot](https://raw.githubusercontent.com/startrug/phptravels-selenium-py/screenshots/logger.png "Logs screenshot")
- the ability to easily generate legible and attractive test reports using Allure (for more look [Generate Test Report](README.md#generate-test-report) section below)
- tests can be run on popular browsers - Chrome and Firefox are preconfigured in DriverFactory class and both can be select in [conftest.py](tests/conftest.py), e.g.
```
@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
```


## Getting Started

Download the project or clone repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Run Automated Tests

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow.

## Generate Test Report

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest --alluredir=./reports
```
After that you need to use command:
```
$ allure serve reports
```
In case, the above command doesnt work, run the below:-
```
$ npm install -g allure-commandline --save-dev
```
Report can be opened via browser.

