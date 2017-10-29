"""Controller class and related functions."""

from train import Train

class Controller:
    """Instantiates and monitors the transportation grid.

    Attributes:
        attr1: herp derp
    """
    def __init__(self):
        Train(00001, IDLING, 0)
        Train(00002, IDLING, 0)
        Train(00003, IDLING, 0)
        Train(00004, IDLING, 0)
        Train(00005, IDLING, 0)
        Train(00006, IDLING, 0)


if __name__ == "__main__":
    # Self-test code
    Controller()
