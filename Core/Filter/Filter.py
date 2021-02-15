from Core.App import App

from Core.Containers.Channel import ChannelContainer, ChannelException
from Core.Helpers import Logger


class Filter:
    def __init__(self, app: App):
        self.app = app
        if self.app.container:
            self.__container = self.app.container
        else:
            Logger.error("app.container is None")
            raise AttributeError("app.container is None")
        if self.app.ftr:
            self.__ftr = self.app.ftr.container
        else:
            Logger.error("app.ftr is None")
            raise AttributeError("app.ftr is None")
        # if Config.NO_REPEAT:
        #         #     self.__no_repeat()
        self.__filter()

    @property
    def container(self) -> ChannelContainer:
        return self.__container

    def __no_repeat(self):
        for item in self.__container:
            for index, item2 in enumerate(self.__container):
                if (item.title in item2.title or item2.title in item.title) and item != item2:
                    del self.__container[index]

    def __check_in_blacklist(self, item, blacklist) -> bool:
        for i in blacklist:
            if i.lower() in item.lower():
                return True
        return False

    def __filter(self):
        output = ChannelContainer()
        blacklist = []
        for ftr in self.__ftr:
            if 'change_group' == ftr.type:
                self.__container.update(ftr.value[0], "group", ftr.value[1])

            if 'required' == ftr.type:
                try:
                    output.append(self.__container.by_name(ftr.value.lower()))
                except ChannelException as e:
                    Logger.info(f'{e}')

            if 'groups' == ftr.type:
                channels_by_group = self.__container.by_group(ftr.value.lower())
                for channel in channels_by_group:
                    output.append(channel)

            if 'blacklist' == ftr.type:
                blacklist.append(ftr.value)

        for item in self.__container:
            if (not self.__check_in_blacklist(item.group, blacklist) and not
                    self.__check_in_blacklist(item.title, blacklist)) and item not in output:
                output.append(item)

        self.__container = output
