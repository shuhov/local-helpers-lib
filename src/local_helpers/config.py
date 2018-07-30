from configparser import RawConfigParser


class Section:
    def __init__(self, params):
        self.__dict__.update(params)

    def __getitem__(self, item):
        return self.__dict__[item]

    def get(self, item, default=None):
        return self.__dict__.get(item, default)


class Config:

    def __init__(self, file_name):
        parser = RawConfigParser()
        parser.optionxform = str
        found = parser.read(file_name)

        if not found:
            raise ValueError('Config file not found!')

        for name in parser.sections():
            self.__dict__.update([(name, Section(parser.items(name)))])

        ConfigStore.register(file_name, self)


class ConfigStore:
    __instance = None
    __holder = dict()

    @staticmethod
    def register(name, config):
        ConfigStore.__holder[name] = config

    @staticmethod
    def names():
        return ConfigStore.__holder.keys()

    def __getitem__(self, item):
        return ConfigStore.__holder[item]

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ConfigStore, cls).__new__(cls)
        return cls.__instance


config_store = ConfigStore()
