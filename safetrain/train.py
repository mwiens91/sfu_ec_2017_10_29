"""Train class and related functions."""

from enum import Enum

class TrainState(Enum):
    """Docstring here."""
    INMOTION = 1
    IDLING = 2
    OOS = 3
    NONE = 4

class Train:
    """Docstring here."""
    def __init__(self, idnum=00000, state=TrainState.NONE, velocity):
        self.idnum = idnum
        self.state = state
        self.velocity = velocity
        self.frontRed = 0
        self.frontYellow = 0
        self.backBlue = 0
    def calculateBuffer(self):
        if self.velocity >= 51:
            self.frontRed = 121.4 + (((velocity-51)/37)*51.8)
            self.frontYellow = 217.3 + (velocity-)

if __name__ == "__main__":
    # Self-test code
    train1 = Train()
