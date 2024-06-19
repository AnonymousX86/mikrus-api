# -*- coding: utf-8 -*-
from enum import Enum
from json import loads as json_loads
from os import getenv

from requests import HTTPError, post

from mikrus.response import *


BASE_URL = 'https://api.mikr.us'


class Endpoint(Enum):
    INFO = 'info'
    SERVERS = 'serwery'
    RESTART = 'restart'
    LOGS_LIST = 'logs'
    LOG_BY_ID = 'logs/ID'
    BOOST = 'amfetamina'
    DATABASES = 'db'
    COMMAND = 'exec'
    STATS = 'stats'
    PORTS = 'porty'
    CLOUD = 'cloud'


class Mikrus:
    def __init__(self, server: str, key: str) -> None:
        self.server: str = server
        self.key: str = key
        # Cache base URL
        self.base_url: str = BASE_URL

    def _request(self, endpoint: Endpoint, params: str = None) -> dict:
        url = f'{self.base_url}/{endpoint.value}'
        request = post(
            url,
            headers={
                'Accept': 'application/json; utf-8'
            },
            data={
                'srv': self.server,
                'key': self.key
            }
        )
        if (code := request.status_code) != 200:
            response = dict(
                error = dict(
                    code = code,
                    message = request.json().get('error', 'Unknown error.')
            ))
        else:
            response = request.json()
        return response

    def info(self) -> MikrusInfo:
        response = self._request(Endpoint.INFO)
        if (error := response.get('error')):
            raise HTTPError(
                error.get('code'),
                error.get('message')
            )
        return MikrusInfo(response)
