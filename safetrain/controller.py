"""Controller class and related functions."""

from . import train

class Controller:
    """Instantiates and monitors the transportation grid.

    Attributes:
        attr1: herp derp
    """
    def __init__(self):
        self.stations = stations
	    self.acceleration = acceleration
	    self.trains = trains
	    train = []
	    
	    if trains > 0:
	        train += Train('00001', IDLING, 0)
	    if trains > 1:
            train += Train('00002', IDLING, 0)
        if trains > 2:
            train += Train('00003', IDLING, 0)
        if trains > 3:
            train += Train('00004', IDLING, 0)
        if trains > 4:
            train += Train('00005', IDLING, 0)
        if trains > 5:
            train += Train('00006', IDLING, 0)

    def initialize_grid():
        index = 0
        
        for station in stations:
            train[index].station = station
            index++
            
            
    def isIntersectionOpen(train):
        """"""
        pass
