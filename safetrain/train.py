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
    def __init__(self, idnum=00000, state=TrainState.NONE):
        self.idnum = idnum
        self.state = state


if __name__ == "__main__":
    # Self-test code
    train1 = Train()
