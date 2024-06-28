import xlsxwriter
import os
import json
import logging
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha, ValidationException, NetworkException, ApiException, TimeoutException


class Captcha:
    """
    A class representing a captcha solver.

    Args:
        url (str): The URL of the webpage containing the captcha.
        driver (webdriver.Chrome): The Chrome webdriver instance.

    Attributes:
        URL (str): The URL of the webpage containing the captcha.
        solution (str): The solution to the captcha.
        driver (webdriver.Chrome): The Chrome webdriver instance.
    """

    def __init__(self, url, driver: webdriver.Chrome) -> None:
        self.URL = url
        self.solution = ''
        self.driver = driver

    def get_sitekey(self):
        """
        Get the sitekey of the captcha.

        Returns:
            str: The sitekey of the captcha.
        """
        g_recaptcha = self.driver.find_element(
            By.CLASS_NAME, 'g-recaptcha'
        )
        self.g_recaptcha = g_recaptcha
        return g_recaptcha.get_attribute('data-sitekey')

    def insert_solution(self):
        """
        Insert the solution to the captcha into the webpage.
        """
        solution = Captcha.solver(self.URL, self.get_sitekey())
        self.driver.execute_script(
            f'document.getElementById("g-recaptcha-response").innerHTML="{solution}";')

    def submit_form(self, submit_button_id):
        """
        Submit the form on the webpage.

        Args:
            submit_button_id (str): The ID of the submit button.
        """
        try:
            button = self.driver.find_element(
                By.ID, submit_button_id
            )
            button.click()
        except Exception as e:
            print('Error al encontrar el form, probablemente en otro frame')
            print(e)
            self.driver.quit()

    @staticmethod
    def solver(url, site_key):
        """
        Solve the captcha using a captcha solving service.

        Args:
            url (str): The URL of the webpage containing the captcha.
            site_key (str): The sitekey of the captcha.

        Returns:
            str: The solution to the captcha.
        """
        key = os.environ.get('API_KEY')
        solver = TwoCaptcha(key)

        try:
            result = solver.recaptcha(
                url=url,
                sitekey=site_key
            )

            return result['code']
        except ValidationException as e:
            print(e)
        except NetworkException as e:
            print(e)
        except ApiException as e:
            print(e)
        except TimeoutException as e:
            print(e)
        return None


def get_driver(url: str) -> webdriver.Chrome:
    """
    Returns a Selenium WebDriver object for the Chrome browser.

    Returns:
        A Selenium WebDriver object for the Chrome browser.
    """
    logging.basicConfig(level=logging.ERROR)
    options = webdriver.ChromeOptions()
    # Disables the sandbox for ChromeDriver
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    # Fixes potential shared memory issues
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    # options.add_argument('--headless')
    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as e:
        print(f"Error: {e}")
        return None

    driver.implicitly_wait(5)
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


def write_json(data, filename):
    """
    Write data to a JSON file.

    Args:
        data (dict): The data to be written to the file.
        filename (str): The name of the file to write the data to.

    Returns:
        None
    """
    with open(f'outputs/{filename}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
