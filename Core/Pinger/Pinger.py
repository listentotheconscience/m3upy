import socket
import time
import requests

from Core.App import App
from Core.Containers.Channel import ChannelContainer
from Core.Helpers import Logger


class Pinger:
    def __init__(self, app: App):
        self.app = app
        self.__container = self.app.container
        self.__ping()

    @property
    def container(self) -> ChannelContainer:
        return self.__container

    def __ping(self):
        for index, item in enumerate(self.__container):
            try:
                requests.get(item.url, timeout=0.1)
            except (socket.timeout, requests.exceptions.RequestException, ValueError):
                Logger.info(f'{item.title} deleted')
                time.sleep(1)
                del self.__container[index]
