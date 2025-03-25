import math 
def calculation(x, y, operation):
    match operation:
        case 'addition':
            return x + y
        case 'substraction':
            return x - y
        case 'division' if y != 0:
            return x / y
        case 'division':
            return ' Cannot divide zero'
        case 'multiplication':
            return x * y
        case 'power':
            return x ** y
        case 'square_ root':
            return math.sqrt(x), math.sqrt(y)
        case _:
            return 'Invalid operation, try again.'
while True: 
    try:
            print('''
                cal: to calculate
                exit to stop   '''.upper())
            option = input("Enter option: ").lower().strip()
            
        
            if option == 'exit':
                    print('Thanks for using our calculator')
                    break
            elif option == "cal": 
                first = float(input("Enter first number: "))
                second = float(input("Enter second number: "))
                operator = input("Enter operator [addition, substraction, multiplation, division, power, square root]: ").strip().lower()
                print(calculation(first, second, operator))
    except ValueError:
        print('wrong input detected, try again.')
        
        
        
        
        
        
        
        
        
        
        