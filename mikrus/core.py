# -*- coding: utf-8 -*-
from enum import Enum

from requests import HTTPError, post

from mikrus.response import *


BASE_URL = 'https://api.mikr.us'


class Endpoint(Enum):
    INFO = 'info'
    SERVERS = 'serwery'
    RESTART = 'restart'
    LOGS_LIST = 'logs'
    LOG_BY_ID = 'logs'
    BOOST = 'amfetamina'
    DATABASES = 'db'
    COMMAND = 'exec'
    STATS = 'stats'
    PORTS = 'porty'
    CLOUD = 'cloud'


class Mikrus:
    def __init__(self, server: str, key: str) -> None:
        self.server: str = server
        self.__key: str = key
        # Cache base URL
        self.base_url: str = BASE_URL

    def _request(
            self,
            endpoint: Endpoint,
            *,
            log_id: int = None
        ) -> dict:
        url = f'{self.base_url}/{endpoint.value}'
        if log_id is not None:
            url += f'/{log_id}'
        headers={
            'Accept': 'application/json; utf-8',
            'Authorization': self.__key
        }
        data={
            'srv': self.server
        }
        request = post(url, headers=headers, data=data)
        if (code := request.status_code) != 200:
            response = dict(
                error = dict(
                    code = code,
                    message = request.json().get('error', 'Unknown error.')
            ))
        else:
            response = request.json()
        try:
            if error := response.get('error'):
                raise HTTPError(
                    error.get('code'),
                    error.get('message')
                )
        except AttributeError:
            pass
        return response

    def info(self) -> MikrusInfo:
        response = self._request(Endpoint.INFO)
        return MikrusInfo(response)

    def servers(self) -> MikrusServerList:
        response = self._request(Endpoint.SERVERS)
        return MikrusServerList(list(response))

    def logs_list(self) -> MikrusLogsList:
        response = self._request(Endpoint.LOGS_LIST)
        return MikrusLogsList(list(response))

    def log_by_id(self, log_id: int) -> MikrusLog:
        response = self._request(Endpoint.LOG_BY_ID, log_id=log_id)
        return MikrusLog(response)
