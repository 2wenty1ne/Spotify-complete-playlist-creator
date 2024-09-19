from dotenv import dotenv_values


def read_env(keyword):
    env_vars = dotenv_values("../../.env")
    return env_vars[f"{keyword}"]


def get_client_id():
    return read_env("CLIENT_ID")


def get_client_secret():
    return read_env("CLIENT_SECRET")


def get_user_id():
    return read_env("USER_ID")
