# -*- coding: utf-8 -*-
from os import getenv

from requests import HTTPError

from mikrus.core import Mikrus


if __name__ == '__main__':
    SEREVR_NAME = getenv('SERVER_NAME')
    API_KEY = getenv('API_KEY')
    server = Mikrus(SEREVR_NAME, API_KEY)
    try:
        info = server.info()
        print(f'Server: {info.server_name} (ID: {info.server_id})')
    except HTTPError as e:
        print(f'Error {e.errno}: {e.strerror}')
