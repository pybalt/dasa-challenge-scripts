from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils import get_driver, Captcha
from utils import write_json


def fill_data(driver: webdriver.Chrome, number: str, year: str, select=None):
    """
    Fill the data in the web form.

    Args:
        driver (webdriver.Chrome): The Chrome webdriver instance.
        number (str): The number to be filled in the form.
        year (str): The year to be filled in the form.
        select (int, optional): The index of the jurisdiction to be selected. If not provided, the user will be prompted to choose one.

    Returns:
        None
    """
    options = Select(driver.find_element(
        By.ID, 'formPublica:camaraNumAni'))

    if select is None:
        jurisdictions = options.options
        [print(i, j.accessible_name) for (i, j) in enumerate(jurisdictions)]
        i_jurisdiction = int(input('Elige un numero para continuar: ').strip())

    else:
        i_jurisdiction = str(select)

    options.select_by_value(str(i_jurisdiction-1))
    driver.find_element(By.ID, 'formPublica:numero').send_keys(number)
    driver.find_element(By.ID, 'formPublica:anio').send_keys(year)


def extract_data(driver: webdriver.Chrome, filter: list) -> dict:
    """
    Extracts data from a web page using the provided driver and filter.

    Args:
        driver (webdriver.Chrome): The Chrome webdriver instance.
        filter (list): A list of labels to filter the data.

    Returns:
        dict: A dictionary containing the extracted data, where the labels are used as keys and the corresponding spans as values.
    """
    data = {}
    form_groups = driver.find_elements(By.CSS_SELECTOR, '.form-group')

    for group in form_groups:
        label = group.find_element(By.CSS_SELECTOR, 'label').text
        span = group.find_element(By.CSS_SELECTOR, 'span').text

        if label in filter:
            data[label[:len(label)-1]] = span

    return data


def entrypoint(url: str, number: str, year: str, filters: list, select=None) -> None:
    """
    Entry point function for the script.

    Args:
        url (str): The URL of the website to scrape data from.
        number (str): The number parameter for the search.
        year (str): The year parameter for the search.
        filters (list): A list of filters to apply to the extracted data.
        select (Optional): An optional parameter for selecting specific elements.

    Returns:
        None
    """
    driver = None
    try:
        driver = get_driver(url)
        fill_data(driver, number, year, select)
        captcha = Captcha(url, driver)

        captcha.insert_solution()
        captcha.submit_form('formPublica:buscarPorNumeroButton')
        write_json(extract_data(driver, filters), 'challenge_a')

    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.quit()
