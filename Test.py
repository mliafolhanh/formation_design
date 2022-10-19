import CheckSolution

#Test calculate max between two

formation1 = CheckSolution.Formation([["L", 0, "L"], [0, 0, 0], [0, "L", 0]])
formation2 = CheckSolution.Formation([["F", 0, 0], [0, "F", 0], [0, 0, "F"]])
formation3 = CheckSolution.Formation([[0, 0, "I"], [0, "I", 0], [0, 0, "I"]])
formation4 = CheckSolution.Formation([[0, 0, "F"], [0, "L", 0], ["F", 0, "L"]])
formation5 = CheckSolution.Formation([["L", 0, "L"], ["I", 0, 0], [0, "I", 0]])
formation6 = CheckSolution.Formation([[0, 0, 0], ["I", "F", 0], [0, "F", "I"]])

validation = CheckSolution.Validation()
solution = CheckSolution.Solution([formation1, formation2, formation3, formation4, formation5, formation6])
print(validation.check(solution))