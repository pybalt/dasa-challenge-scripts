# Challenge C Documentation

This document provides an overview of key functionalities within the script, focusing on external dependencies and their roles in the implementation. This guide is intended to be read as part of a technical interview to understand the use of third-party libraries in our project.

## External Dependencies

### requests (2.32.3)

- **Usage**: Utilized within the `API` class methods (`get` and `post`).
- **Purpose**: Facilitates making HTTP requests to interact with the API. The `requests` library is used to send GET and POST requests to the API endpoints, allowing the script to retrieve and submit data effectively.

### json (standard library)

- **Usage**: Used for encoding and decoding JSON data.
- **Purpose**: Converts Python objects to JSON format and vice versa. The `json` library is used to handle the data exchanged between the script and the API, ensuring proper data formatting for requests and responses.