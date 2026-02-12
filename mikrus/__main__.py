# -*- coding: utf-8 -*-
from os import getenv

from requests import HTTPError

from mikrus.core import Mikrus


if __name__ == '__main__':
    SERVER_NAME = getenv('SERVER_NAME')
    API_KEY = getenv('API_KEY')
    server = Mikrus(SERVER_NAME, API_KEY)
    try:
        info = server.info()
        print(f'Server: {info.server_name} (ID: {info.server_id})')
        server_list = server.servers()
        print(f'Server list: {', '.join(map(str, server_list.servers)) if server_list else 'None'}')
        logs = server.logs_list()
        print(f'Server logs: {str(logs) if logs else 'None'}')
        print(f'Last log: {server.log_by_id(logs[0].id) if logs else 'None'}')
        databases = server.databases()
        print(f'Databases: {str(databases) if databases else 'None'}')
    except HTTPError as e:
        print(f'Error {e.errno}: {e.strerror}')
