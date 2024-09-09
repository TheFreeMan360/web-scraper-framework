import requests

from scraper_framework.adapter.interface_driver import IDriver


class RequestsDriver(IDriver):
    def __init__(self) -> None:
        super().__init__()

    def get(self, url: str) -> None:
        # return requests.get(url, headers=play_load)
        return requests.get(url)

    def close(self) -> None:
        # del
        pass
