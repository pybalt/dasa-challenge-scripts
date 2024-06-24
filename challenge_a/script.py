from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from utils import get_driver, take_screenshot
from time import sleep


def extract_data(driver: webdriver.Chrome, number: str, year: str) -> dict:
    options = Select(driver.find_element(By.ID, 'formPublica:camaraNumAni'))
    jurisdictions_selector = options.options
    jurisdictions = []
    for j in jurisdictions_selector:
        jurisdictions.append(j)
    print('Elige una juridiccion')
    [print(i, j.accessible_name) for (i, j) in enumerate(jurisdictions)]
    i_jurisdiction = input('Elige un numero para continuar: ').strip()
    if not (int(i_jurisdiction) in range(len(jurisdictions))):
        return extract_data(driver, number, year)

    options.select_by_value(i_jurisdiction)
    number_input = driver.find_element(By.ID, 'formPublica:numero')
    number_input.send_keys(number)

    year_input = driver.find_element(By.ID, 'formPublica:anio')
    year_input.send_keys(year)

    captcha = driver.find_element(
        By.ID, 'formPublica:recaptcha-publico:reCaptcha')

    take_screenshot(
        _bytes=captcha.screenshot_as_png
    )

    sleep(5)

    submit_button = driver.find_element(
        By.ID, 'formPublica:buscarPorNumeroButton')
    submit_button.click()

    sleep(30)


def entrypoint(url: str, number: str, year: str) -> None:
    driver = get_driver(url)
    extract_data(driver, number, year)
