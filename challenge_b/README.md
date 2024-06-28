# CHALLENGE B SCRIPT DOCUMENTATION

This document provides an overview of key functionalities within the script, focusing on external dependencies and their roles in the implementation. This guide is intended to be read as part of a technical interview to understand the use of third-party libraries in my project.

## External Dependencies

### selenium (4.22.0)

- **Usage**: Extensively used throughout the `challenge_b/script.py`.
- **Purpose**: Facilitates interaction with web browsers for automation tasks. Specifically, it is used to:
  - Initialize the web driver (`webdriver.Chrome`).
  - Locate and interact with web elements such as input fields (`find_element(By.ID, "bar")`) and buttons (`find_element(By.ID, "startsearchBtn")`).
  - Extract data from the webpage, such as tables (`find_element(By.ID, "tbl_member")` and `find_element(By.TAG_NAME, "tbody")`).

### XlsxWriter (3.2.0)

- **Usage**: Utilized within the `create_excel` function from the `utils` module.
- **Purpose**: Generates Excel files to store the extracted data. This library allows the creation of structured and formatted Excel spreadsheets, making the data easily accessible and presentable.