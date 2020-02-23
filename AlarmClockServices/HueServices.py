#!/usr/bin/env python
from qhue import Bridge, QhueException, create_new_username
from ConfigServices import ConfigServiceImpl
import configparser

class HueServiceImpl:

    CONFIG_FILE_PATH = 'alarm_clock.ini'
    SECTION_NAME = 'hue'
    IP_OPTION_NAME = 'ip'
    USERNAME_OPTION_NAME = 'username'

    def __init__(self):
        config = ConfigServiceImpl()
        ip = config.getOption(ConfigServiceImpl.HUE_SECTION, ConfigServiceImpl.IP_OPTION)
        username = config.getOption(ConfigServiceImpl.HUE_SECTION, ConfigServiceImpl.USERNAME_OPTION)

        if(username is None):
            username = self.getUsername(ip)
            config.setOption(ConfigServiceImpl.HUE_SECTION, ConfigServiceImpl.USERNAME_OPTION, username)

        self.bridge = Bridge(ip, username)

    def getUsername(self, ip):
        while True:
            try:
                username = create_new_username(ip)
                break
            except QhueException as err:
                print("Error occurred while creating a new username: {}".format(err))
        return username

    def doRoutine(self, transitionMins):
        transitionTime = transitionMins * 600
        self.bridge.groups(1, 'action', on=True, bri=1, sat=254)
        self.bridge.groups(1, 'action', bri=254, sat=0, transitiontime=int(transitionTime))



def main():
    hueService = HueServiceImpl()
    hueService.doRoutine(10)

if __name__ == "__main__":
    main()
