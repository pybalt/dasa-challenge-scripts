from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import xlsxwriter
import logging


def get_driver() -> webdriver.Chrome:
    """
    Returns a Selenium WebDriver object for the Chrome browser.

    Returns:
        A Selenium WebDriver object for the Chrome browser.
    """
    logging.getLogger('selenium').setLevel(logging.ERROR)
    logging.getLogger('urllib3').setLevel(logging.ERROR)

    URL = "https://www.osbar.org/members/membersearch_start.asp"
    options = webdriver.ChromeOptions()
    # Disables the sandbox for ChromeDriver
    options.add_argument('--no-sandbox')
    # Fixes potential shared memory issues
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as e:
        print(f"Error: {e}")
        return None

    driver.implicitly_wait(15)
    driver.get(URL)
    return driver


def create_excel(data: dict):
    """
    Creates an Excel file from the data.

    Args:
        data: The data to write to the Excel file.
    """
    workbook = xlsxwriter.Workbook('outputs/challenge_b.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0

    for key, value in data.items():
        worksheet.write(row, col, key)
        worksheet.write(row + 1, col, value)
        col += 1
    workbook.close()


def extract_data(driver: webdriver.Chrome, bar_number: str):
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


def entrypoint(bar_number):
    """
    The entry point for the challenge.

    This function is called when the script is run from the command line.
    """
    driver = get_driver()

    if driver is None:
        return

    data = extract_data(driver, bar_number=bar_number)
    create_excel(data)
    driver.quit()
