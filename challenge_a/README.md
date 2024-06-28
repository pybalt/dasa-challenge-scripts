# Challenge A Documentation

This document provides an overview of the `script.py` file in the `challenge_a` directory, focusing on the justification for the installed libraries used in the script. This guide is intended to be read as part of a technical interview to understand the use of third-party libraries in my project.

## External Dependencies

### selenium (4.22.0)

- **Usage**: Extensively used throughout the `script.py`.
- **Purpose**: Selenium is a powerful tool for web browser automation. In this script, it is used to:
  - Launch a browser and navigate to the specified URL (`get_driver(url)`).
  - Locate and interact with web elements such as dropdowns, text fields, and buttons (`By.ID`, `By.CSS_SELECTOR`).
  - Automate the process of filling out a form and submitting it.

### 2captcha-python (1.2.7)

- **Usage**: Utilized within the `Captcha` class to solve CAPTCHAs.
- **Purpose**: Integrates with the 2Captcha service to automatically solve CAPTCHA challenges encountered during web automation. This is crucial for ensuring the script can progress past CAPTCHA verifications without manual intervention.

### python-dotenv (1.0.1)

- **Usage**: Implicitly used to load environment variables.
- **Purpose**: Facilitates the secure management of sensitive information such as API keys by loading them from a `.env` file. This ensures that sensitive data is not hard-coded into the script, enhancing security and flexibility.

### json (standard library)

- **Usage**: Used for encoding and decoding JSON data.
- **Purpose**: Converts Python objects to JSON format and vice versa. The `json` library is used to handle the data exchanged between the script and the API, ensuring proper data formatting for requests and responses.