import requests
from requests.exceptions import HTTPError
import re

from Core.App import App
from Core.Config.exceptions import ConfigKeyErrorException
from Core.Containers.Channel import ChannelContainer, Channel
from Core.Helpers import Logger


class Parser:
    def __init__(self, app: App):
        self.app = app
        if self.app.config['PLAYLIST_URLS']:
            self.__url = self.app.config['PLAYLIST_URLS']
        else:
            Logger.error('PLAYLIST_URLS does not exist')
            raise ConfigKeyErrorException('PLAYLIST_URLS does not exist')
        self.__container = ChannelContainer()
        self.__parse()

    @property
    def container(self):
        return self.__container

    @property
    def __contents(self) -> str:
        output = ''
        for url in self.__url:
            try:
                r = requests.get(url)
                output += r.text + '\n'
            except HTTPError as e:
                Logger.error(f'{url} is not reachable')
        return output

    @property
    def __listed(self) -> list:
        return self.__contents.split("\n")

    def __verify_title(self, item: str) -> str:
        if item.startswith("#EXTINF"):
            item = item.split(',')[-1].strip()
            return item
        return ''

    def __verify_group(self, item: str) -> str:
        if item.startswith("#EXTINF"):
            if "group-title" in item:
                group = re.search(r'group-title="[a-zA-Zа-яёА-ЯЁ0-9-+\s.]+"', item)
                if group:
                    group = group.group().split('=')[1]
                    group = re.sub(r'"', '', group)
                    return group.strip()
        elif item.startswith("#EXTGRP"):
            group = item.split(':')[-1].strip()
            return group
        return ''

    def __verify_vlcopt(self, item) -> str:
        if item.startswith('#EXTVLCOPT'):
            vlcopt = item.split(":")[-1].strip()
            return vlcopt
        return ''

    def __verify_url(self, item) -> str:
        if item.startswith('http'):
            return item.strip()
        return ''

    def __parse(self):
        title = group = vlcopt = url = ''
        for item in self.__listed:
            if title == '':
                title = self.__verify_title(item)
            if group == '' or group == self.app.config['UNSORTED']:
                group = self.__verify_group(item)
                group = group if group else self.app.config['UNSORTED']
            if vlcopt == '':
                vlcopt = self.__verify_vlcopt(item)
            if url == '':
                url = self.__verify_url(item)

            if title != '' and group != '' and url != '':
                self.__container.append(Channel(title, group, vlcopt, url))
                title = group = vlcopt = url = ''
