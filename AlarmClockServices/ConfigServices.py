import configparser

class ConfigService:

    CONFIG_FILE = 'alarm_clock.ini'

    HUE_SECTION = 'hue'
    IP_OPTION = 'ip'
    USERNAME_OPTION = 'username'

    def __init__(self, filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    def __init__(self):
        self.__init__(self.CONFIG_FILE)

    def getOption(self, section, option):
        try:
            return self.config.get(section, option)
        except Exception:
            return None
