from pathlib import Path


class Config(dict):
    def __init__(self):
        defaults = {
            'ROOT_DIR': str(Path(__file__).parent.parent.parent),
            'DEBUG': False,
            'LOG_PATH': str(Path(__file__).parent.parent.parent.joinpath('Log')),
            'TEST_PATH':  str(Path(__file__).parent.parent.parent.joinpath('Test')),
            'LOG_FILENAME': "{date}-{level}.log"
        }
        dict.__init__(self, defaults)

    def from_object(self, obj):
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)