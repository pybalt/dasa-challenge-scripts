import requests
import json


class API:

    BASE_URL = 'https://eje.juscaba.gob.ar/iol-api/api/public/expedientes'

    @staticmethod
    def get(sub_url: str, params: str):
        return requests.get(f"{API.BASE_URL}/{sub_url}", params=params)

    @staticmethod
    def post(sub_url: str, params: str, payload: object):
        return requests.post(f"{API.BASE_URL}/{sub_url}", params=params, data=payload)

    @staticmethod
    def get_list(filter: json):
        payload = {'info': json.dumps(filter)}
        data = API.post("lista", params=None, payload=payload)
        data.raise_for_status()

        return data.json()

    @staticmethod
    def get_record_details(exp_id: int):
        data = API.get("ficha",
                       params={"expId": exp_id})
        data.raise_for_status()

        return data.json()


def get_first(identificador: str):

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
    return {
        'id': id,
        'fecha': data['fechaInicio'],
        'caratula': data['caratula'],
        'materia': data['objetosJuicio'][0]['materia'],
        'objeto': data['objetosJuicio'][0]['objetoJuicio']
    }


def write_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    number = input("Input a number: ")
    data = get_first(number)
    write_json(data, 'challenge_c/output.json')
