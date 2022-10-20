from typing import Tuple
from xmlrpc.client import Boolean
import CheckSolution
import Constant
class Tool:
    def __init__(self):
        """
            0: F
            1: I
            2: L
            3: F I
            4: I L
            5: F L
        """
        self.candidates = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        self.initPoolCandidate()
        print(len(self.candidates[0]))
        print(len(self.candidates[1]))
        print(len(self.candidates[2]))
        print(len(self.candidates[3]))
        print(len(self.candidates[4]))
        print(len(self.candidates[5]))

    def append(self, type: int, value: int):
        self.candidates[type].append(value)

    def initPoolCandidate(self):
       
        for value in range(Constant.MaxEncryptValue):
            formation = CheckSolution.Formation.decrypt(value)
            typeCandidate = self.checkCandidate(formation)
            if typeCandidate != -1:
                self.append(typeCandidate, value)
       
       
    def checkCandidate(self, formation: CheckSolution.Formation) -> int:
        """
            The candidates should have exact 1 or 2 diffrent types in [F, I, L]
            No more than 4 of cell different from 0 and no less than 3
        """        
        numberApp = {}
        for dx in range(Constant.MaxW):
            for dy in range(Constant.MaxH):
                numberApp[formation.matrix[dx][dy]] = numberApp.get(formation.matrix[dx][dy], 0) + 1
        
        # whether number character different from 0 is more than 0
        numberCellsNotZero = Constant.MaxW * Constant.MaxH - numberApp.get(0, 0)
        if numberCellsNotZero != 4:
            return -1

        keys = numberApp.keys()
        mainKeys = self.getMainKeys(keys)
        # number keys should not be more than 3
        if len(keys) > 3:
                return -1

        # # if 3 then should have 1 key
        # if numberCellsNotZero == 3:
        #     if len(keys) != 2:
        #         return -1

        # if 4 then should have 2 key
        if numberCellsNotZero == 4:
            if len(keys) == 3:       
                if numberApp[mainKeys[0]] != numberApp[mainKeys[1]]:
                    return -1
        return self.getType(mainKeys)

    def getMainKeys(self, keys) :
        result = []
        for key in keys:
            if key != 0:
                result.append(key)
        return result

    def getType(self, mainKeys):
        if len(mainKeys) == 1:
            return Constant.SkillMapToInt[mainKeys[0]] - 1;
        combineKey = mainKeys[0] + mainKeys[1]
        if combineKey == "FI" or combineKey == "IF":
            return 3
        if combineKey == "LI" or combineKey == "IL":
            return 4
        if combineKey == "FL" or combineKey == "LF":
            return 5

    def recursive(self, top, listOfSolution, currentResult, currentType):
        # print(currentResult)
        # print(currentType)
        if len(listOfSolution) > top:
            return
        if currentType >= Constant.NumberOfFormations:
            formations = [CheckSolution.Formation.decrypt(value) for value in currentResult]
            listOfSolution.append(CheckSolution.Solution(formations))
            print(currentResult)
            return 
        for candidate in self.candidates[currentType]: 
            if self.checkACandiateForType(currentResult, candidate):
                self.recursive(top, listOfSolution, currentResult + [candidate], currentType + 1)

    def checkACandiateForType(self, currentResult, candidate)->bool:    
        validation = CheckSolution.Validation()
        candidateForm = CheckSolution.Formation.decrypt(candidate)
        for value in currentResult:
            formation = CheckSolution.Formation.decrypt(value)
            if not validation.validateTwoFormation(formation, candidateForm):
                return False 
        return True
                    
    
tool = Tool()
listOfSolution = []
tool.recursive(1, listOfSolution, [], 0)
for solution in listOfSolution: 
    print(solution)

