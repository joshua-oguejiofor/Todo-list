import json as js
student_grade = 'student grade.js'
def load_file():
    try:
    
        with open(student_grade, 'r') as file:
            return js.load(file)
    except (FileNotFoundError, js.JSONDecodeError):
        return []
def save_file(student):
    with open(student_grade,'w') as file:
        return js.dump(student,file,indent=4)
    

def add_record(student):
    try:
        subject = input("Enter subject:\n").lower().strip()
        user_add1 = str(input("Enter student name:\n").lower().strip())
        if user_add1.isalpha():
            pass
        else:
            print('Please enter a valid name.')
        user_add2 = int(input("Enter student score:\n").strip())
        if user_add2 >= 70:
            user_add2 = (f''' 
Score: {user_add2} 
{'grade: A'}
''')
        elif user_add2 >= 60:
            user_add2 = (f'''
Score: {user_add2}
{'grade: B'}
''')
        elif user_add2 >=50:
            user_add2 = (f'''
Score:{user_add2} 
{'grade: C'}
''')
        elif user_add2 >= 40:
            user_add2 = (f'''
Score: {user_add2} 
{'grade: D'}
''')
        elif user_add2 >=30:
            user_add2 = (f'''
Score: {user_add2}
{'grade: E'}
''')  
        elif user_add2 >=0:
            user_add2 =(f'''
Score: {user_add2} 
{'grade: F'}
''') 
        student.append({'subject':subject,'name':user_add1,'score':user_add2})
        save_file(student)
        print("Details added.")
    except ValueError:
        print('Wrong input.')
        
def view_record(student):
    if not student:
        print("No data found.")
    else:
        for i, student in enumerate(student, 1):
            print(f'''
{i}. Subject: {student['subject']}
Name: {student['name']} 
{student['score']}
''')
            
def search_record(student):
    user_search = input("Enter student name:\n").lower().strip()
    result = [student for student in student if user_search in student['name']]
    if result:
        for student in result:
            print('Search result.')
            print(f'''
Subject: {student['subject']} 
Name: {student['name']} 
Score:{ student['score']}''')

def delete_record(student):
    view_record(student)
    try:
        user_delete = int(input("Enter number to delete:\n").strip()) -1
        student.pop(user_delete)
        save_file(student)
        print("Deleted.")
    except (ValueError, IndexError):
        print('Wronge input.')
 

           
def main():
    record = load_file()
    while True:
        print('''
              Students score.
1. add details.
2. view details.
3. search details.
4. delete details.
5. 6exit
    '''.upper())
        choice = input("Enter your option:\n").lower().strip()
        if choice == '1':
            add_record(record)
        elif choice == '2':
            view_record(record)
        elif choice == '3':
            search_record(record)
        elif choice == '4':
            delete_record(record)
        elif choice == '5':
            print('Good bye, see you again.')
            break
        else:
            print('Invalid input.')

main()