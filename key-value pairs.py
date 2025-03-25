import json as js
value_file = 'value.py'

def load_file():
    try:
        with open(value_file, 'r') as file:
            return js.load(file)
    except (FileNotFoundError, js.JSONDecodeError):
        return []
    
def save_file(value):
    with open(value_file, 'w') as file:
        return js.dump(value, file, indent=4)
    
def add_file(value):
    while True:
        name = str(input("Enter name:\n").lower().strip())
        date_of_birth = input("Enter date of birth:\n").strip()
        contry = str(input("Enter your country:\n").lower().strip())
        if name or date_of_birth or contry == 'exit':
            break
        else:
            value.append({'name': name, 'DOB': date_of_birth,'origen': contry})
        print('Added successfully')

    
        
                                                