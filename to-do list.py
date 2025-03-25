import json as js
task_file = 'task.js'
def load_file():        
        try:
                with open(task_file, 'r') as file:
                        return js.load(file)    # convert json data to python list 
        except (FileNotFoundError, js.JSONDecodeError):
                return [] #return an empty list if no file is found
def save_file(task):
        with open(task_file, 'w') as file:
              return js.dump(task, file, indent=4)      # convert python list to json fomat and save
      
# Allows user to input and save the task, also handle error.
def add_task(task):
        try:
              user_task = input("Enter task to save:\n").strip()
              task.append({'task': user_task, 'completed': False})
              save_file(task)
              print(f'Task {user_task} added.')
        except ValueError:
                print("Invalid input")
                
# Allow user to search for task
def search_task(task):
        try:
                 
                user_search = input("Enter task to search:\n").lower().strip()
                feed_back = [task for task in task if user_search in task['task']]
                if feed_back:
                        for task in feed_back:
                                status = '[Done]' if task['completed'] else '[Not done]'
                                print('Search result:')
                                print(f'{task['task']} {status}')
                else:
                        print(f'NO task "{user_search}"')
                        
                       
        except ValueError:
                print('Invalid input.')
 
# Allow user to view all task               
def view_task(task):
        if not task:
                print('No task avalible')
        else:
                for i, task in enumerate(task, 1):
                        status = '[Done]' if task['completed'] else '[Not done]'
                        print(f'{i}. {task['task']} {status} ')

# Allow user to mark completed task                       
def mark_task(task):
        view_task(task)
        try: 
                user_mark = int(input("Enter task to mark completed: \n") )-1
                if 0 <= user_mark < len(task):
                        task[user_mark]['completed'] = True
                        save_file(task) 
                        print(f'Task "{task[user_mark]['task']}" marked complete')
                else:
                        print('Invalid input')
        except ValueError:
                print('Please enter a valid number.') 

# Allow user to delete task                       
def delete_task(task):
        view_task(task)
        try:
                user_delete = int(input("Enter task number to delete: \n") )-1
                if 0 <= user_delete < len(task):
                        task.pop(user_delete)
                        save_file(task)
                        print(f'Task  deleted')
                else:
                        print('Please enter a valid number.') 
        except ValueError:
                print('Please enter a valid number.')

# main function to run all codes                                               
def main():
        task = load_file()
        while True:
                print('''
                to-do list.
enter your option to begin.
1. add task.
2. view task.
3. mark task.
4. delete task.
5. search task     
6. exit
        '''. upper())
                try:
                        choice = int(input("Enter your choice: \n"))
                        if choice ==  1:
                                add_task(task) 
                        elif choice == 2:
                                view_task(task)
                        elif choice == 3:
                                mark_task(task)
                        elif choice == 4:
                                delete_task(task)
                        elif choice == 5:
                                search_task(task)
                        elif choice == 6:
                                print('Exiting.....Good Bye')
                                break
                except ValueError:
                        print('Please enter a valid number.')
                        
main()                 # To run all program.               


                