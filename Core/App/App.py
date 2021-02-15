from Core.Config import Config
from Core.Config.exceptions import ConfigKeyErrorException
from Core.Dropbox import Authorize
from Core.Dropbox.exceptions import DropboxAuthorizeException
from Core.Helpers import Logger
from Core.Filter import FilterParser, Filter
from Core.Pinger import Pinger
from Core.Parser import Parser


class App:
    def __init__(self):
        self.config = Config()
        self.__dbx = None
        self.__parser = None
        self.__filter = None
        self.__pinger = None
        self.__container = None
        self.ftr = None

    @property
    def container(self):
        return self.__container

    def dropbox_connect(self):
        if self.config['DBX_ACCESS_TOKEN']:
            try:
                self.__dbx = Authorize(self.config['DBX_ACCESS_TOKEN'])
            except DropboxAuthorizeException as e:
                Logger.error(f'Dropbox error: {e}')
        raise ConfigKeyErrorException('DBX_ACCESS_TOKEN does not exist')

    def register_module(self, module):
        if isinstance(module, Filter):
            self.__filter = module
            self.__container = self.__filter.container
        elif isinstance(module, Parser):
            self.__parser = module
            self.__container = self.__parser.container
        elif isinstance(module, Pinger):
            self.__parser = module
            self.__container = self.__parser.container
        elif isinstance(module, FilterParser):
            self.ftr = module
        else:
            Logger.error(f'Undefined module class: {module.__class__.__name__}')
            raise AttributeError(f'Undefined module class: {module.__class__.__name__}')
