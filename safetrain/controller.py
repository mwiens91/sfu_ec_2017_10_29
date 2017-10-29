"""Controller class and related functions."""

from . import train


class Controller:
    """Instantiates and monitors the transportation grid.

    Attributes:
        attr1: herp derp
    """
    def __init__(self, stationids, idnums):
        """stationids and idnums are lists of strings; the strings contain numbers."""
        self.roadlengths = {1: 15e3, 2: 20e3, 3: 25e3}
        self.intersections = {1: [15e3/2, 20e3/3], 3: [25e3/2, 20e3*2/3]}
        self.stationidpositions = {1101: 0, 1501: self.roadlengths[1],
                                   2101: self.roadlengths[2], 2501: 0,
                                   3101: 0, 3501: self.roadlengths[3]}

        self.trainlist = []

        for stationid, idnum in zip(stationids,idnums):
            self.trainlist += [trainTrain(self, int(idnum),
                                                int(stationid[0]),
                                                float(self.stationidpositions[stationid]))]

    def isIntersectionOpen(self, train_):
        """Test if upcoming intersection for a given train is empty."""
        # Find which train we're testing for
        if train_.road == 2:
            # If train 2, test which intersection coming next.
            # Test for intersection 1,2 first
            if ((train_.position < self.intersections[1][1] and train_.velocity > 0)
              or (train_.position < self.intersections[3][1] and train_.position > [1][1] and train_.velocity < 0)):
                # Train 2 approaching 1st intersection. Test whether
                # train 1 in intersection
                for train1 in trainlist:
                    if train1.road == 1:
                        if train1.position > self.intersections[1][0] and train1.position - train1.length < self.intersections[1][0]:
                            return False
                        else:
                            return True

                # No train on track 1
                return True
            elif ((train_.position > self.intersections[3][1] and train_.velocity < 0)
              or (train_.position > self.intersections[1][1] and train_.position < [3][1] and train_.velocity > 0)):
                # Train 2 approaching 1st intersection. Test whether
                # train 3 in intersection
                for train3 in trainlist:
                    if train3.road == 1:
                        if train3.position > self.intersections[3][0] and train3.position - train3.length < self.intersections[3][0]:
                            return False
                        else:
                            return True

                # No train on track 3
                return True
            else:
                # Not approaching an intersection
                return True
        elif train_.road == 1:
            for train2 in trainlist:
                if train2.road == 2:
                    if train2.position > self.intersections[1][1] and train3.position - train3.length < self.intersections[1][1]:
                        return False
                    else:
                        return True

            # No train on track 2
            return True
        else:
            for train2 in trainlist:
                if train2.road == 2:
                    if train2.position > self.intersections[3][1] and train3.position - train3.length < self.intersections[3][1]:
                        return False
                    else:
                        return True

            # No train on track 2
            return True

    def distanceToIntersection(self, train_):
        # Find which train we're testing for
        if train_.road == 2:
            # If train 2, test which intersection coming next.
            # Test for intersection 1,2 first
            if ((train_.position < self.intersections[1][1] and train_.velocity > 0)
              or (train_.position < self.intersections[3][1] and train_.position > [1][1] and train_.velocity < 0)):
                return train_.position - self.intersections[1][1]
            elif ((train_.position > self.intersections[3][1] and train_.velocity < 0)
              or (train_.position > self.intersections[1][1] and train_.position < [3][1] and train_.velocity > 0)):
                return train_.position - self.intersections[3][1]
            else:
                # Not approaching an intersection
                return -1
        elif train_.road == 1:
            if train_.position < self.intersections[1][1]:
                return self.intersections[1][1] - train_.position
            else:
                return -1
        else:
            if train_.position < self.intersections[3][1]:
                return self.intersections[3][1] - train_.position
            else:
                return -1
