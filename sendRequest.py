import requests


def send_request(r_type, url, headers=None, params=None, data=None):

    if r_type == "post":
        # print(f"Sending post request to {url}")
        response = requests.post(url, headers=headers, data=data)

    elif r_type == "get":
        # print(f"Sending get request to {url}")
        response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print('Error:', response.status_code)
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

