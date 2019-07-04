import  ShareAnalysisScipts.generator_randomwalk as rw
import ShareAnalysisScipts.config_Type as config

# pytest test_RandomWalkGenerator.py


def simpleDice3PositiveMock(arg):
    return 1

class TestCalcWalk(object):
  

    def test_WalkInitialisedCorrectly(self):
        startWalk = 1
        data = 1
        configWalker = config.WalkerConfig(data , 100, 100)
        
        cut = rw.RandomWalker(configWalker, start= startWalk)
        walk = cut.calcWalk()
        assert walk[0] == startWalk
        assert len(walk) == data 

    def test_WalkIsComputedCorrectly_MonotonicalGrowth(self):
        startWalk = 1
        steps = 2
        configWalker = config.WalkerConfig(steps, 100, 100)
        expectedWalk = [startWalk, startWalk * (1 + simpleDice3PositiveMock(0)/100)]
        cut = rw.RandomWalker(configWalker,startWalk)
        walk = cut.calcWalk(
            dice1= lambda a: 2,
            dice2= lambda a: 3,
            dice3= simpleDice3PositiveMock)
        assert walk[0] == expectedWalk[0]
        assert walk[1] == expectedWalk[1]
        assert len(walk) == steps
        for step in walk:
            assert step > 0

    def test_WalkIsComputedCorrectly_MonotonicalFalling(self):
        startWalk = 1
        steps = 2
        configWalker = config.WalkerConfig(steps, 100, 100)
        expectedWalk = [startWalk, startWalk / (1 + simpleDice3PositiveMock(0)/100)]
        cut = rw.RandomWalker(configWalker,startWalk)
        walk = cut.calcWalk(
            dice1= lambda a: 3,
            dice2= lambda a: 2,
            dice3= simpleDice3PositiveMock)
        assert walk[0] == expectedWalk[0]
        assert walk[1] == expectedWalk[1]
        assert len(walk) == steps
        for step in walk:
            assert step > 0