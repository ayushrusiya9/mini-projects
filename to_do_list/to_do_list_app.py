while True:
    choice = int(input("-- TODO LIST MENU --\n1. Add Task\n2. View Tasks\n3. Delete Tasks\n4. Exit \nENTER ANY NUMBER : "))

    if choice == 1:
        # add task
        task = input("ENTER TASK: ")
        with open('todo.txt', 'a') as file:
            file.write(task + '\n')
            print('Task added', task)
       

    elif choice == 2:
        #view task
        try:
            with open('todo.txt','r') as file:
                tasks = file.readlines()
                if not tasks :
                    print("No task found!")
                else:
                    print("YOUR TODO LIST TASKS!")
                    for i, tasks in enumerate(tasks, start=1):
                        print(f'{i}.{tasks.strip()}')
        
        except FileNotFoundError:
            print(" 'todo.txt' file does not exist")

    elif choice == 3:
        # delete task
        try:
            with open('todo.txt','r') as file:
                tasks = file.readlines()
            if not tasks:
                print("No task found!")
            else:
                print("YOUR TODO LIST TASKS!")
                for i,task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            
            task_num = int(input("ENTER TASK NUMBER : "))

            if 1 <= task_num <= len(tasks):
                # tasks = list(tasks)
                
                removed = tasks.pop(task_num - 1)
                with open("todo.txt",'w') as file:
                    file.writelines(tasks)
                    print(f"task deleted: {removed.strip()}")
            else:
                print("INVALID NUMBER!!!!!")
        except FileNotFoundError:
            print("FILE NOT FOUND!!!!!!!!!")

    elif choice == 4:
        # exit
        break