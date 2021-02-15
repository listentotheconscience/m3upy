import os
from datetime import datetime
from Core.Config import Config

class Logger:
    PADDING = 9
    cfg = Config()
    @classmethod
    def __setup_logger(cls, level: str):
        if not os.path.exists(cls.cfg['LOG_PATH']):
            os.mkdir(cls.cfg['LOG_PATH'])
        filename = os.path.join(cls.cfg['LOG_PATH'], cls.__fill_template_string(level))
        return open(filename, 'a', encoding='utf-8')

    @classmethod
    def __fill_template_string(cls, level: str):
        date = datetime.now()
        date = date.strftime('%d-%m-%Y')
        return cls.cfg['LOG_FILENAME'].format(date=date, level=level)

    @classmethod
    def __log(cls, level, message):
        if level is None or message is None:
            raise AttributeError("level and message must exist")
        file = cls.__setup_logger(level=level)
        time = datetime.now().strftime('%H:%M')
        file.write(f'|{level.ljust(cls.PADDING)}|{time}| {message}\n')
        file.close()

    @classmethod
    def debug(cls, message: str):
        cls.__log(level="DEBUG", message=message)

    @classmethod
    def info(cls, message:str):
        cls.__log(level="INFO", message=message)

    @classmethod
    def warning(cls, message: str):
        cls.__log(level="WARNING", message=message)

    @classmethod
    def error(cls, message: str):
        cls.__log(level="ERROR", message=message)

    @classmethod
    def critical(cls, message: str):
        cls.__log(level="CRITICAL", message=message)
