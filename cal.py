import math
import os

previous_ans = False
ans = 0
exit_status = False
options = ['+','-','*','/','^','√']

def removeDot(num):
    if num == int(num):
        return int(num)
    return num
def getInput(is_one_input, operator):
    if previous_ans and is_one_input:
        return ans
    elif is_one_input or previous_ans:
        while True:
            try:
                num = input('Enter a number: ')
                if num == '':
                    continue
                num = removeDot(float(num))
                if num == 0 and operator == 4:
                    print('Cannot divide by zero.')
                    continue
                elif num < 0 and operator == 6:
                    print('Cannot square root a negative number.')
                    continue
                elif ans < 0 and num != int(num) and operator == 5:
                    print('Cannot calculate non integer exponent of negative number.')
                    continue
                break
            except:
                print('Invalid input!')
                continue
        return [ans,num] if previous_ans else num
    while True:
        try:
            num1 = input('Enter first number: ')
            if num1 == '':
                continue
            num1 = removeDot(float(num1))
            break
        except:
            print('Invalid input!')
            continue
    while True:
        try:
            num2 = input('Enter second number: ')
            if num2 == '':
                continue
            num2 = removeDot(float(num2))
            if num2 == 0 and operator == 4:
                print('Cannot divide by zero.')
                continue
            elif num1 < 0 and num2 != int(num2) and operator == 5:
                print('Cannot calculate non integer exponent of negative number.')
                continue
            break
        except:
            print('Invalid input')
            continue
    return [num1, num2]

print('''
Python Calculator

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exponentiation (^)
6. Square root (√)
7. Exit
 ''')
while not exit_status:
        try:
            option = input('Type an option [1,2,3,4,5,6,7]: ')
            if option == '':
                continue
            option = int(option)
            if not (option >= 1 and option <= 7):
                raise Exception('Invalid input!')
        except:
            print('Invalid input!')
            continue
        if option == 7:
            break
        values = getInput(False, option) if option < 6 else getInput(True, option)
        if option == 1:
            print('Your answer is',values[0],options[option-1],values[1],'=',removeDot(values[0]+values[1]))
            ans = values[0]+values[1]
        elif option == 2:
            print('Your answer is',values[0],options[option-1],values[1],'=',removeDot(values[0]-values[1]))
            ans = values[0]-values[1]
        elif option == 3:
            print('Your answer is',values[0],options[option-1],values[1],'=',removeDot(values[0]*values[1]))
            ans = values[0]*values[1]
        elif option == 4:
            print('Your answer is',values[0],options[option-1],values[1],'=',removeDot(values[0]/values[1]))
            ans = values[0]/values[1]
        elif option == 5:
            print('Your answer is',values[0],options[option-1],values[1],'=',removeDot(pow(values[0],values[1])))
            ans = pow(values[0],values[1])
        else:
            if previous_ans and ans < 0:
                print('Cannot square root a negative number.')
                continue
            print('Your answer is',options[option-1]+str(values),'=',removeDot(math.sqrt(values)),'\n')
            ans = math.sqrt(values)

        print('''
1.Clear
2.Calculate by answer
''')
        while True:
            try:
                option2 = input('Type an option [1,2]: ')
                if option2 == '':
                    continue
                option2 = int(option2)
                if option2 == 1:
                    ans = 0
                    previous_ans = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif option2 == 2:
                    previous_ans = True
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print('Invalid input!')
                    continue
                print('''
Python Calculator

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exponentiation (^)
6. Square root (√)
7. Exit
 ''')
            except:
                print('Invalid input!')
                continue
            break