# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


NULL_DATETIME = datetime.min.isoformat()


def optional_datetime(timestamp: str) -> datetime | None:
    if timestamp:
        return datetime.fromisoformat(timestamp)
    return None


class MikrusServer:
    def __init__(self, payload: dict) -> None:
        self.server_id: str = payload.get('server_id')
        self.server_name: str = payload.get('server_name')
        self.expires: datetime = datetime.fromisoformat(payload.get('expires'))
        self.param_ram: int = int(payload.get('param_ram', 0))
        self.param_disk: int = int(payload.get('param_disk', 0))

    def __str__(self) -> str:
        return self.server_id

    def __repr__(self) -> str:
        return (
            f'Mikrus(' +
            f'id="{self.server_id}", ' +
            f'expires="{self.expires}", ' +
            f'ram="{self.param_ram}", ' +
            f'hdd="{self.param_disk}")'
        )


class MikrusServerInfo(MikrusServer):
    def __init__(self, payload: dict) -> None:
        super().__init__(payload)
        self.imie_id: str = payload.get('imie_id')
        self.expires_storage: datetime | None = optional_datetime(payload.get('expires_storage'))
        self.last_login: datetime = datetime.fromisoformat(payload.get('lastlog_panel'))
        self.mikrus_pro: bool = payload.get('mikrus_pro', 'nie') != 'nie'


class MikrusServerList:
    def __init__(self, payload: list[dict]) -> None:
        self.servers = []
        for data in payload:
            self.servers.append(MikrusServer(data))

    def __str__(self) -> str:
        return f'[{', '.join(map(str, self.servers))}]'

    def __getitem__(self, item: int) -> MikrusServer:
        return self.servers[item]


class MikrusRestart:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusLog:
    def __init__(self, payload: dict) -> None:
        self.id: int = int(payload.get('id', 0))
        self.server_id: str = payload.get('server_id')
        self.task: str = payload.get('task')
        self.created: datetime = datetime.fromisoformat(payload.get('when_created'))
        self.done: datetime | None = optional_datetime(payload.get('when_done'))
        self.output: str = payload.get('output')

    @property
    def time(self) -> timedelta | None:
        if not isinstance(self.created, datetime) or not isinstance(self.done, datetime):
            return None
        return self.created - self.done

    def __str__(self) -> str:
        return f'{self.id}:{self.task}'

    def __repr__(self) -> str:
        return (
            f'MikrusLog(' +
            f'id="{self.id}", ' +
            f'server_id="{self.server_id}", ' +
            f'task="{self.task}")'
        )


class MikrusLogsList:
    def __init__(self, payload: list[dict]) -> None:
        self.logs = []
        for data in payload:
            self.logs.append(MikrusLog(data))

    def __str__(self) -> str:
        return f'[{', '.join(map(str, self.logs))}]'

    def __getitem__(self, item: int) -> MikrusLog:
        return self.logs[item]


class MikrusBoost:
    def __init__(self, payload: dict) -> None:
        self.payload = payload


class MikrusDatabase:
    def __init__(self, db_type: str, payload: str) -> None:
        self.type: str = db_type
        rows = payload.split('\n')
        self.server: str = rows[0].split(': ')[1]
        self.login: str = rows[1].split(': ')[1]
        self.password: str = rows[2].split(': ')[1]
        self.base: str = rows[3].split(': ')[1]

    def __str__(self) -> str:
        return f'{self.type}://{self.login}@{self.server}/{self.base}'

    def __repr__(self) -> str:
        return (
            f'MikrusDatabase(' +
            f'server="{self.server}", ' +
            f'login="{self.login}", ' +
            f'base="{self.base}")'
        )


class MikrusDatabaseList:
    def __init__(self, payload: dict) -> None:
        self.databases = []
        for data in payload.keys():
            self.databases.append(MikrusDatabase(data, payload[data]))

    def __str__(self):
        return f'[{', '.join(map(str, self.databases))}]'

    def __getitem__(self, item: str) -> MikrusDatabase:
        for database in self.databases:
            if database.type == item:
                return database
        raise KeyError(item)


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
