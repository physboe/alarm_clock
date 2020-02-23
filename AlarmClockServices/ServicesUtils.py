from abc import ABC, abstractmethod


class RoutineInterface(ABC):

    @abstractmethod
    def doRoutine(self, args):
        pass
