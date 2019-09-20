from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def do_login(driver, login, password):
    WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, ".auth-controls__btn_login.btn-signin"))
    )
    driver.find_element_by_css_selector('.auth-controls__btn_login.btn-signin').click()
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "site-auth-content"))
    )
    driver.find_element_by_css_selector('site-auth-content .user-credentials-form__item:nth-child(1) input').send_keys(login)
    driver.find_element_by_css_selector('site-auth-content .user-credentials-form__item:nth-child(2) input').send_keys(password)

    driver.find_element_by_css_selector('site-auth-content .user-credentials-form__btn').click()

    assert WebDriverWait(driver, 5).until(
        ec.invisibility_of_element_located((By.CSS_SELECTOR, "site-auth-content"))
    )
