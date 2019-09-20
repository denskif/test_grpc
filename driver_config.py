from selenium import webdriver
from utils.urls import SITE_URL


def get_driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1366, 1053)
    driver.get(SITE_URL)
    return driver
