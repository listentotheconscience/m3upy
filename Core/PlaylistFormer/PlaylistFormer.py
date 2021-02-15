from Core.Containers.Channel import ChannelContainer


class PlaylistFormer:
    def __init__(self, container: ChannelContainer):
        self.__container = container

    @property
    def m3u_string(self) -> str:
        string = '#EXTM3U\n\n'
        for item in self.__container:
            string += f'#EXTINF:-1,{item.title.title()}\n'
            string += f'#EXTGRP:{item.group}\n'
            string += f'#EXTVLCOPT:{item.vlcopt}\n' if item.vlcopt else ''
            string += f'{item.url}\n\n'
        return string

    def form(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.m3u_string)
