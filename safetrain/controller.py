"""Controller class and related functions."""

from . import train

class Controller:
    """Instantiates and monitors the transportation grid.

    Attributes:
        attr1: herp derp
    """
    def __init__(self, stationids, idnums):
        self.trainlist = []

        for stationid, idnum in zip(stationids,idnums):
            self.trainlist += [trainTrain(self, idnum, station, 

    def isIntersectionOpen(train_):
        pass

    def distanceToIntersection(train_):
        pass
