# DASA AUTOMATION SCRIPTS

Welcome to the repository for the DASA web scraping challenges. This repository contains scripts developed to demonstrate my abilities in reverse engineering websites, automating data extraction, and bypassing CAPTCHA protections to access information typically protected from bot extraction.

## Overview

This repository is organized into several challenges, each represented by a separate directory. Each directory contains a `script.py` file that performs specific web scraping tasks, demonstrating the use of various third-party libraries and techniques for data extraction.

## Challenges

### Challenge A

- **Objective**: Automate the process of filling out a web form, solving CAPTCHA challenges, and extracting specific data from the resulting webpage.
- **Key Libraries**:
  - `selenium`: Used for web browser automation, including form filling and interaction with web elements.
  - `2captcha-python`: Integrates with the 2Captcha service to solve CAPTCHA challenges.
  - `python-dotenv`: Manages environment variables securely, ensuring sensitive data such as API keys are not hard-coded.
  - `json` (standard library): Used for encoding and decoding JSON data.

### Challenge B

- **Objective**: Extract data from a web page and generate an Excel report.
- **Key Libraries**:
  - `selenium`: Used for web browser automation, including data extraction from web elements.
  - `XlsxWriter`: Generates Excel files to store extracted data in a structured format.

### Challenge C

- **Objective**: Interact with an API to retrieve and submit data.
- **Key Libraries**:
  - `requests`: Facilitates making HTTP requests to interact with the API.
  - `json` (standard library): Used for encoding and decoding JSON data.

## Getting Started

To get started with the scripts in this repository, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/pybalt/dasa-challenge-scripts.git
   cd dasa-challenge-scripts
   ```

2. **Set up a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add the necessary environment variables, such as API keys, required by the scripts.

5. **Run the scripts**:
   - Navigate to the root directory of the repository.
   - Execute the main file:
     ```sh
     python app.py
     ```

## Conclusion

This repository showcases my ability to perform web scraping tasks using Python, Selenium, and other relevant libraries. It demonstrates my skills in automating web interactions, handling CAPTCHA challenges, and extracting and processing data efficiently.

For any questions or further discussion, feel free to reach out via my GitHub profile or email.