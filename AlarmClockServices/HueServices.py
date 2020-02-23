#!/usr/bin/env python

from os import path
from qhue import Bridge, QhueException, create_new_username
import configparser

class HueServiceImpl:

    CONFIG_FILE_PATH = 'alarm.ini'
    SECTION_NAME = 'hue'
    IP_OPTION_NAME = 'ip'
    USERNAME_OPTION_NAME = 'username'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(self.CONFIG_FILE_PATH)
        self.bridge = self.getBridge(config)

    def getBridge(self, config):
        ip = config.get(self.SECTION_NAME, self.IP_OPTION_NAME)
        try:
            username = config.get(self.SECTION_NAME,self.USERNAME_OPTION_NAME)
        except Exception as expt:
            while True:
                try:
                    username = create_new_username(ip)
                    config.set(self.SECTION_NAME, self.USERNAME_OPTION_NAME, username)
                    config.write(self.CONFIG_FILE_PATH)
                    break
                except QhueException as err:
                    print("Error occurred while creating a new username: {}".format(err))

        return Bridge(ip, username)

    def doRoutine(self, transitionMins):
        transitionTime = transitionMins * 600
        self.bridge.groups(1, 'action', on=True, bri=1, sat=254)
        self.bridge.groups(1, 'action', bri=254, sat=0, transitiontime=int(transitionTime))



def main():
    hueService = HueServiceImpl()
    hueService.doRoutine(10)

if __name__ == "__main__":
    main()
