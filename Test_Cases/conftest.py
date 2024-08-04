import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        raise ValueError("Browser not supported: {}".format(browser))
    yield driver
    driver.quit()

def pytest_addoption(parser):  # Corrected function name
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture()
def browser(request):  # this will return browser value to the setup method
    return request.config.getoption("--browser")

#HTML Report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    # Ensure the 'pytest-html' plugin is installed and enabled
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'Stethup'
        config._metadata['Module Name'] = 'Jobs'
        config._metadata['Tester'] = 'Dinesh Aravinth'


# It is hook for delete/Modify Environment info to HTML
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop ("JAVA_HOME", None)
    metadata.pop("Plugins", None)