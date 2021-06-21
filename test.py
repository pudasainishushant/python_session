# import flask
from simple_calculator import add_num,sub_num

num1 = 5
num2 = 4
program = input("What program is this? /n")


if program == "Calculator":
    decision = input("Addition or Subtraction")
    if decision == "Addition":   
        addition_result = add_num(num1,num2)
        print(addition_result")
    else:
        result = sub_num(num1,num2)
        print(result)
elif program == "Printer":
    print("hahha")
else:
    print("Yo print garxa ani tyo loop bata pass hunxa")
    pass



"""
if onekeystroke == "forward" and secondkeystroke == "a":
    staetment 1 gadi agadi badaune statemnt
    staemtn 2
elif condition2:
    stamtnemt 3
    statemtn 4
elif condition3:
    statemtn 5
else:
    statemtn 6

"""