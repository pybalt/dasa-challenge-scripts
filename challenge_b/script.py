from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import get_driver, create_excel


def extract_data(driver: webdriver.Chrome, bar_number: str) -> dict:
    """
    This function performs the extraction of data from a website using Selenium.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        bar_number (str): The bar number to search for.

    Returns:
        dict: A dictionary containing the extracted data.
    """
    data = {}

    bar_input = driver.find_element(By.ID, "bar")
    bar_input.send_keys(f"{bar_number}")
    search_button = driver.find_element(By.ID, "startsearchBtn")
    search_button.click()

    table = driver.find_element(By.ID, "tbl_member")
    body = table.find_element(By.TAG_NAME, "tbody")
    body_rows = body.find_elements(By.TAG_NAME, "tr")
    data['Name'] = body.find_element(By.CLASS_NAME, "adminheader").text

    cell_data = {}
    for row in body_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) == 2 and cells[0].text != "":
            key = cells[0].text
            value = cells[1].text
            cell_data[key.strip()] = value

    data['Company'] = cell_data.get('Company', "")
    data['Email'] = cell_data.get('Email', "")

    return data


def entrypoint(bar_number: str, url: str) -> None:
    """
    The entry point for the challenge.

    This function is called when the script is run from the command line.

    Parameters:
        bar_number (int): The number of the bar to extract data for.

    Returns:
        None
    """
    driver = get_driver(url)

    if driver is None:
        return

    data = extract_data(driver, bar_number=bar_number)
    create_excel(data)
    driver.quit()
