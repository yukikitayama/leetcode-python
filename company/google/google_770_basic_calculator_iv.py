




# Input:
expression = "e - 8 + temperature - pressure"
evalvars = ["e", "temperature"]
evalints = [1, 12]
# Output: ["-1*pressure","5"]
"""
1 - 8 + 12 - pressure = 5 - pressure
"""
# Input:
expression = "a * b * c + b * a * c * 4"
evalvars = []
evalints = []
# Output: ["5*a*b*c"]


