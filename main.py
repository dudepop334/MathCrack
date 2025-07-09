import math

print("== MathCrack ==")

  number1 = float(input("first number: "))
  Mathsymbol = input("+, -, *, /: ")
  number2 = float(input("second number: "))

  if Mathsymbol == "+":
result = number1 + number2
  elif Mathsymbol == "-":
result = number1 - number2
  elif Mathsymbol == "*":
result = number1 * number2
  elif Mathsymbol == "/":
result = number1 / number2
  else:
result = "Error"
  else:
  result = "Error"

  print(f"\n{number1} {Mathsymbol} {number2} = {result}")
