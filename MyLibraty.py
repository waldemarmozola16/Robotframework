from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver import Remote  # Remote imported only for code completion
import logging


def get_current_browser():
    """
    :rtype: Remote
    """
    browser = BuiltIn().get_library_instance('Selenium2Library')._current_browser()
    return browser


def get_title_via_python():
    driver = get_current_browser()
    title = driver.title
    driver.find_elemrnt_by_class_name()
    logging.warn("checking title %s" % title)
    return title


def get_my_window_size():
    driver = get_current_browser()
    size = driver.get_window_size()
