import requests

from App.data.CustomExceptions import RequestTypeNotFoundException


def send_request(r_type, url, headers=None, params=None, data=None, json_data=None):

    if r_type == "post":
        # print(f"Sending post request to {url}") #TEST
        response = requests.post(url, headers=headers, data=data, json=json_data)

    elif r_type == "get":
        # print(f"Sending get request to {url}") #TEST
        response = requests.get(url, headers=headers, params=params)

    else:
        raise RequestTypeNotFoundException(r_type)


    if response.status_code == 200:
        return response.json()
    else:
        print('Error:', response.status_code)
        print(response.json())
        return 0


def clear_whitespaces(obj_to_clean):

    if isinstance(obj_to_clean, str):
        return obj_to_clean.replace(" ", "").replace("\t", "").replace("\n", "")

    elif isinstance(obj_to_clean, dict):
        for key, value in obj_to_clean.items():
            obj_to_clean[key] = clear_whitespaces(value)
        return obj_to_clean
    else:
        return obj_to_clean

