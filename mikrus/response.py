# -*- coding: utf-8 -*-
class MikrusInfo:
    def __init__(self, payload: dict) -> None:
        self.server_id: str = payload.get('server_id')
        self.server_name: str = payload.get('server_name')
        self.expires: str = payload.get('expires')
        self.expires_cytrus: str = payload.get('expires_cytrus')
        self.expires_storage: str = payload.get('expires_storage')
        self.param_ram: int = int(payload.get('param_ram', 0))
        self.param_disk: int = int(payload.get('param_disk', 0))
        self.last_login: str = payload.get('lastlog_panel')


class MikrusServer:
    def __init__(self, payload: dict) -> None:
        self.server_id: str = payload.get('server_id')
        self.server_name: str = payload.get('server_name')
        self.expires: str = payload.get('expires')
        self.param_ram: int = int(payload.get('param_ram', 0))
        self.param_disk: int = int(payload.get('param_disk', 0))


class MikrusRestart:
    def __init__(self, payload: dict) -> None:
        self.payload = payload
class MikrusServerList:
    def __init__(self, payload: list[dict]) -> None:
        self.servers = []
        for data in payload:
            self.servers.append(MikrusServer(data))


class MikrusLogsList:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusLog:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusBoost:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusDatabases:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusCommand:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusStats:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusPorts:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusCloud:
    def __init__(self, payload: dict) -> None:
        self.payload = payload
