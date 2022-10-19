from ast import For
from ctypes import sizeof
from shutil import ExecError
from typing import Tuple
from xmlrpc.client import Boolean
import Constant


class Formation:
    def __init__(self, matrix):
        """
            matrix: List[List[int]] with size is W * H
        """
        self.matrix = matrix

    def encrypt(self) -> int:
        """
            Encrypt a formation into number with 4 base(0->0, F->1, I->2, L->3)
        """
        value = 0
        for dx in range(Constant.MaxW):
            for dy in range(Constant.MaxH):
                value = value * 4 + Constant.SkillMapToInt[self.matrix[dx][dy]]
        return value       

    def decrypt(value):
        matrix = [[0 for i in range(Constant.MaxH)] for j in range(Constant.MaxW)]
        for dx in range(Constant.MaxW - 1, -1, -1):
            for dy in range(Constant.MaxH - 1, -1, -1):
                matrix[dx][dy] = Constant.IntMapToSkill[value % 4]
                value = value // 4
        return Formation(matrix)

    def __str__(self) -> str:
        result = ""
        for dx in range(Constant.MaxW):
            for dy in range(Constant.MaxH):
                if self.matrix[dx][dy] != 0:
                    result += self.matrix[dx][dy]
                else :
                    result += "0"
            result += "\n"
        return result

class Solution:
    def __init__(self, formations):
        """
            formations: List[Formation]
        """
        self.formations = formations

    def __len__(self) -> int:
        return len(self.formations)

    def __repr__(self) -> str:
        result = "Solution: \n"
        for formation in self.formations:
            result += "\n{}".format(formation)
        return result
    
class Validation:
    def check(self, solution: Solution) -> Tuple:
        # Step 1: Validate each input
        for formulation in solution.formations:
            self.checkInput(formulation)

        # Step 2: Validate each pairs
        maxResult = 0
        violatePairs = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                tmpResult = self.calculateMaxCommonBetweenTwo(solution.formations[i], solution.formations[j]) 
                maxResult = max(maxResult, tmpResult)
                if tmpResult > Constant.MaxCommon:
                    violatePairs.append((i, j))
        return (maxResult, maxResult <= Constant.MaxCommon, violatePairs)

    def checkInput(self, formation: Formation):
        if len(formation.matrix) != Constant.MaxW:
            raise Exception("Formation has wrong width")
        for i in range(Constant.MaxW):
            if len(formation.matrix[i]) != Constant.MaxH:
                raise Exception("Formation has wrong height")
            for j in range(Constant.MaxH):
                if not (formation.matrix[i][j] in Constant.SkillCharacters):
                    raise Exception("The character " + formation.matrix[i][j] + " is not in the list " + Constant.SkillCharacters) 

    def validateTwoFormation(self, firstFormation: Formation, secondFormation: Formation) -> int:
        return self.calculateMaxCommonBetweenTwo(firstFormation, secondFormation) <= Constant.MaxCommon

    def calculateMaxCommonBetweenTwo(self, firstFormation: Formation, secondFormation: Formation) -> int:

        #Step1 : check (firstFormation, secondFormation)
        result1 = self.calculateMaxCommonBetweenOrderTwo(firstFormation, secondFormation)    

        #Step2 : check (secondFormation, firstFormation)
        result2 = self.calculateMaxCommonBetweenOrderTwo(secondFormation, firstFormation)
        return max(result1, result2)    

    def calculateMaxCommonBetweenOrderTwo(self, firstFormation: Formation, secondFormation: Formation) -> int:
        result = 0
        for dx in range(Constant.MaxW - 1, -1, -1):
            for dy in range(Constant.MaxH - 1, -1, -1):
                if (self.isShareBetweenTwo(firstFormation, secondFormation, (dx, dy))):
                    result = max(result, (Constant.MaxW - dx) * (Constant.MaxH - dy))
        return result

    def isShareBetweenTwo(self, firstFormation: Formation, secondFormation: Formation, startPoint: Tuple) -> Boolean:
        for dx in range(startPoint[0], Constant.MaxW):
            for dy in range(startPoint[1], Constant.MaxH):
                projectedX = dx - startPoint[0]
                projectedY = dy - startPoint[1]
                if firstFormation.matrix[projectedX][projectedY] != 0 and secondFormation.matrix[dx][dy] != 0:
                    if firstFormation.matrix[projectedX][projectedY] != secondFormation.matrix[dx][dy]:
                        return False 
        return True
