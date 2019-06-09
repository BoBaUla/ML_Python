import ShareAnalysisScipts.eva_Memory as mem
# pytest test_memory.py
memoryValues = [0,1,2,3,4,5,6,7,8,9]
steps = 3

class TestMemory(object):

    def test_SetMemory_AddsValues_ResetsValues(self):
        mem.setMemory(memoryValues[1])
        assert mem.memory[0] == memoryValues[1]
        assert len(mem.meanMemory) == len(mem.memory)
        assert len(mem.stdMemory) == len(mem.memory)
        mem.resetAll()
        assert len(mem.memory) == 0
        assert len(mem.meanMemory) == 0
        assert len(mem.stdMemory) == 0
        

    def test_SetMemory_AddsValues(self):
        mem.resetMemory()
        for i in range(len(memoryValues)-steps+1):
            mem.setMemory(memoryValues[i+steps-1])
        assert len(mem.memory) == len(memoryValues)-steps+1
        assert len(mem.meanMemory) == len(mem.memory)
        assert len(mem.stdMemory) == len(mem.memory)
        mem.resetAll()
    

    