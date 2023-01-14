def is_one_digit(num):
    return (num > -10) and (num < 10) and (num.is_integer())

def check(num1, num2, oper):
    msg = ""
    if is_one_digit(num1) and is_one_digit(num2):
        msg += " ... lazy"
    if (num1 == 1 or num2 == 1) and (oper == '*'):
        msg += " ... very lazy"
    if (num1 == 0 or num2 == 0) and (oper in ('*', '+', '-')):
        msg += " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)

memory = 0
while True:
    print("Enter an equation")
    calc = input()
    x, oper, y = calc.split()
    result = None

    try:
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        
        x, y = float(x), float(y)
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/':
            result = x / y
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        
        if result or result == 0:
            print(result)
            print("Do you want to store the result? (y / n):")
            answer = input()
            if answer == 'y':
                if is_one_digit(result):
                    one_digit_msgs = ["Are you sure? It is only one digit! (y / n)", 
                                 "Don't be silly! It's just one number! Add to the memory? (y / n)",
                                 "Last chance! Do you really want to embarrass yourself? (y / n)"
                                ]
                
                    for index, msg in enumerate(one_digit_msgs):
                        print(msg)
                        answer = input()
                        if answer == 'n':
                            break
                        if index == 2:
                            memory = result
                
                else:
                    memory = result
                             
            print("Do you want to continue calculations? (y / n):")
            answer = input()
            if answer == 'n':
                break
    
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
