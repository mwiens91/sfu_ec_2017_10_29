"""Train class and related functions."""

from enum import Enum

class TrainState(Enum):
    """Simple enumerator which holds state of train."""
    INMOTION = 1
    IDLING = 2
    OOS = 3
    NONE = 4

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
    def __init__(self, idnum=00000, state, velocity):
        """Initialize train variables."""
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
