import generator_randomwalk as rw
# pytest test_RandomWalkGenerator.py


def simpleDice3PositiveMock(arg):
    return 1

class TestCalcWalk(object):
  

    def test_WalkInitialisedCorrectly(self):
        startWalk = 1
        steps = 1
        cut = rw.RandomWalker(startWalk, maxStep= 0)
        walk = cut.calcWalk(steps = steps)
        assert walk[0] == startWalk
        assert len(walk) == steps + 1

    def test_WalkIsComputedCorrectly_MonotonicalGrowth(self):
        startWalk = 1
        steps = 1
        expectedWalk = [startWalk, startWalk * (1 + simpleDice3PositiveMock(0)/100)]
        cut = rw.RandomWalker(startWalk, maxStep= 0)
        walk = cut.calcWalk(
            steps = steps, 
            dice1= lambda a: 2,
            dice2= lambda a: 3,
            dice3= simpleDice3PositiveMock)
        assert walk[0] == expectedWalk[0]
        assert walk[1] == expectedWalk[1]
        assert len(walk) == steps + 1
        for step in walk:
            assert step > 0

    def test_WalkIsComputedCorrectly_MonotonicalFalling(self):
        startWalk = 1
        steps = 1
        expectedWalk = [startWalk, startWalk / (1 + simpleDice3PositiveMock(0)/100)]
        cut = rw.RandomWalker(startWalk, maxStep= 0)
        walk = cut.calcWalk(
            steps = steps, 
            dice1= lambda a: 3,
            dice2= lambda a: 2,
            dice3= simpleDice3PositiveMock)
        assert walk[0] == expectedWalk[0]
        assert walk[1] == expectedWalk[1]
        assert len(walk) == steps + 1
        for step in walk:
            assert step > 0
