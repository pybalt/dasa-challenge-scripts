import xlsxwriter
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote import webelement
from selenium import webdriver


def get_driver(url: str) -> webdriver.Chrome:
    """
    Returns a Selenium WebDriver object for the Chrome browser.

    Returns:
        A Selenium WebDriver object for the Chrome browser.
    """
    options = webdriver.ChromeOptions()
    # Disables the sandbox for ChromeDriver
    options.add_argument('--no-sandbox')
    # Fixes potential shared memory issues
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    # options.add_argument('--headless')

    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as e:
        print(f"Error: {e}")
        return None

    driver.implicitly_wait(15)
    driver.get(url)
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


def take_screenshot(driver: webdriver.Chrome = None, _bytes: bytes = None):

    sc = None

    if driver is not None:

        sc = driver.get_screenshot_as_png()

    if _bytes is not None:

        sc = _bytes

    with open('outputs/screenshot.png', 'wb') as f:
        f.write(sc)
