import configparser

class ConfigServiceImpl:

    CONFIG_FILE = 'alarm_clock.ini'

    HUE_SECTION = 'hue'
    IP_OPTION = 'ip'
    USERNAME_OPTION = 'username'

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE)

    def getOption(self, section, option):
        try:
            return self.config.get(section, option)
        except Exception:
            return None

    def setOption(self, section, option, value):
        self.config.set(section, option, value)
        self.config.write(self.CONFIG_FILE)
