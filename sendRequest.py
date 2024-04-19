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
