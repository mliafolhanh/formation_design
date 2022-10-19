# formation_design
For checking and generate formations

## Notation of skill
- L: ligtening
- F: fire
- I: ice

## Constant(refer to Constant.py file)
- MaxW = 3
- MaxH = 3
- MaxCommon = 4
- NumberOfFormations = 6

## Formation 
- Matrix size is 3 * 3
- Intialization: formation = CheckSolution.Formation([["L", 0, "L"], [0, 0, 0], [0, "L", 0]])

## Solution:
- List of formation
- Initalization: soluton = CheckSolution.Soluton([...])

## Validation:
- validation = CheckSolution.Validation()
- validation.check(solution:Solution): return a tuple, first is maximum value of collision, second is a boolean indicate the solution valid, the third is list of formation pair which violate the condition
