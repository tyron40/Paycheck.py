User_paycheck = float(input('enter pay amount:'))
User_hours= float(input('Hours worked:'))
Hours_limit = 40
Total_calculated = (User_hours * User_paycheck)
Invalid = False
if User_hours <= Hours_limit:
    print('$', Total_calculated, "expected")
else:
    Invalid = True
    if Invalid:
        print(' invalid hours')
Warnings = 0
Warning_limit = 3
User_input2 = int(input(' How many warnings have you received? '))
if User_input2 <= Warning_limit:
    print('Good standing!')
else:
    print('you need to go to HR!')
User_input = (input(' Who is Your area manager? '))
if User_input == ('Andrew'):
    print('Tell Andrew to come to HR!')
elif User_input == ("John"):
    print('Your on the wrong shift')
else:
    print('Invalid input')




