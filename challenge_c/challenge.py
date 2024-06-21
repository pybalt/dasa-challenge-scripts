import requests
import json


class API:
    """
    A class that provides methods for interacting with an API.

    Attributes:
        BASE_URL (str): The base URL of the API.

    Methods:
        get(sub_url: str, params: str): Sends a GET request to the specified sub URL with the given parameters.
        post(sub_url: str, params: str, payload: object): Sends a POST request to the specified sub URL with the given parameters and payload.
        get_list(filter: json): Retrieves a list of records based on the provided filter.
        get_record_details(exp_id: int): Retrieves the details of a specific record based on the provided ID.
    """

    BASE_URL = 'https://eje.juscaba.gob.ar/iol-api/api/public/expedientes'

    @staticmethod
    def get(sub_url: str, params: str):
        """
        Sends a GET request to the specified sub URL with the given parameters.

        Args:
            sub_url (str): The sub URL to send the request to.
            params (str): The parameters to include in the request.

        Returns:
            The response object from the GET request.
        """
        return requests.get(f"{API.BASE_URL}/{sub_url}", params=params)

    @staticmethod
    def post(sub_url: str, params: str, payload: object):
        """
        Sends a POST request to the specified sub URL with the given parameters and payload.

        Args:
            sub_url (str): The sub URL to send the request to.
            params (str): The parameters to include in the request.
            payload (object): The payload to include in the request.

        Returns:
            The response object from the POST request.
        """
        return requests.post(f"{API.BASE_URL}/{sub_url}", params=params, data=payload)

    @staticmethod
    def get_list(filter: json):
        """
        Retrieves a list of records based on the provided filter.

        Args:
            filter (json): The filter to apply to the records.

        Returns:
            The JSON response containing the list of records.
        """
        payload = {'info': json.dumps(filter)}
        data = API.post("lista", params=None, payload=payload)
        data.raise_for_status()

        return data.json()

    @staticmethod
    def get_record_details(exp_id: int):
        """
        Retrieves the details of a specific record based on the provided ID.

        Args:
            exp_id (int): The ID of the record to retrieve.

        Returns:
            The JSON response containing the details of the record.
        """
        data = API.get("ficha", params={"expId": exp_id})
        data.raise_for_status()

        return data.json()


def get_first(identificador: str):
    """
    Retrieves the first record based on the given identifier.

    Args:
        identificador (str): The identifier used to filter the records.

    Returns:
        dict: The curated data for the first record.

    Raises:
        KeyError: If the 'content' key or 'expId' key is not found in the API response.
    """

    filter = {
        'filter': json.dumps({'identificador': identificador}),
        'tipoBusqueda': 'CAU',
        'page': 0,
        'size': 10
    }

    data = API.get_list(filter)
    exp_id = data['content'][0]['expId']
    details = API.get_record_details(exp_id)

    return curate_data(exp_id, details)


def curate_data(id, data: dict):
    """
    Curates the given data dictionary and returns a curated data dictionary.

    Args:
        id (any): The ID of the data.
        data (dict): The data dictionary to be curated.

    Returns:
        dict: The curated data dictionary.

    """
    return {
        'id': id,
        'fecha': data['fechaInicio'],
        'caratula': data['caratula'],
        'materia': data['objetosJuicio'][0]['materia'],
        'objeto': data['objetosJuicio'][0]['objetoJuicio']
    }


def write_json(data, filename):
    """
    Write data to a JSON file.

    Args:
        data (dict): The data to be written to the file.
        filename (str): The name of the file to write the data to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def entrypoint(number: str):
    """
    This is the entrypoint function for the challenge_c script.
    It prompts the user to input a number, retrieves data using the `get_first` function,
    and writes the data to a JSON file using the `write_json` function.
    """
    data = get_first(number)
    write_json(data, 'outputs/challenge_c.json')
