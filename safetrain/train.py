"""Train class and related functions."""

from . import controller
from enum import Enum

class TrainState(Enum):
    """Simple enumerator which holds state of train."""
    INMOTION = 1
    IDLING = 2
    OOS = 3
    EMR = 4

class Train:
    """Represents a train on the transportation grid.

    Attributes:
        idnum: A five digit integer containing the trains identification number.
        state: A TrainState instance which indicates whether the train
            is in motion, idling, or out of service.
        velocity: A float representing the velocity of the train. This
            is a signed number; i.e., a negative sign means the train is
            travelling west or south.
        frontRed: A float representing the front red buffer of the
            train. If this buffer contacts another train's rear blue buffer,
            then an emergency stop will be performed.
        frontYellow: A float representing the front yellow buffer of the
            train. If this buffer contacts another train's rear blue
            buffer, then the train will be slowed down.
        backBlue: A float representing the rear blue buffer, which
            interacts with frontRed and frontYellow above.
    """
    def __init__(self, controller, idnum, state):
        """Initialize train variables."""
        self.controller = controller
        self.idnum = idnum
        self.state = state
        self.velocity = 0
        self.acceleration = 9.8
        self.maxSlowAmount = -9.8
        self.position = 0

        self.frontRed = 0
        self.frontYellow = 0
        self.backBlue = 0


    def calculateBuffer(self):
        if self.velocity >= 51:
            self.frontRed = 121.4 + (((self.velocity-51)/37)*51.8)
            self.frontYellow = 217.3 + (((self.velocity-51)/37)*85.1)
            self.backBlue = 82.15 - (((self.velocity - 51)/37)*12.95)
        elif self.velocity >= 31:
            self.frontRed = 88.75 + (((self.velocity-31)/19)*23.75)
            self.frontYellow = 162 + (((self.velocity-31)/19)*38)
            self.backBlue = 89.15 - (((self.velocity - 31)/19)*(-6.65))
        elif self.velocity >= 1:
            self.frontRed = 51.1 + (((self.velocity-1)/30)*31.9)
            self.frontYellow = 101.8 + (((self.velocity-1)/30)*52.2)
            self.backBlue = 99.65 - (((self.velocity - 1)/30)*(-10.15))
        else:
            self.frontRed = 50
            self.frontYellow = 100
            self.backBlue = 100


    def getTrainState(self):
        return self.state

    def bufferIsClear(self):
        if self.yellowZoneIsEmpty() and self.redZoneIsEmpty():
            return True
        return False


    def yellowZoneIsEmpty(self):
        if self.controller.distanceToIntersection() <= self.frontYellow and self.controller.isIntersectionOpen():
            return True
        return False

    def redZoneIsEmpty(self):
        if self.controller.distanceToIntersection() <= self.frontRed and self.controller.isIntersectionOpen():
            return True
        return False

    def eStop(self):
        while self.redZoneIsEmpty():
            self.changeSpeed(self.maxSlowAmount)

    def eSlow(self):
        while self.yellowZoneIsEmpty():
            self.changeSpeed(self.maxSlowAmount)

    def speedUp(self):
        if self.velocity < 88.5:
            self.changeSpeed(self.acceleration)


    def changeSpeed(self, delta):
        if self.velocity + delta > 88.5:
            self.velocity = 88.5
        elif self.velocity + delta < 0:
            self.velocity = 0
        else:
            self.velocity += delta




if __name__ == "__main__":
    # Self-test code
    train1 = Train()
