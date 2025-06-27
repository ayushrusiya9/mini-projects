while True:
    choice = int(input("-- TODO LIST MENU --\n1. View Tasks\n2. Add Tasks\n3. Delete Tasks\n4. Exit \nENTER ANY NUMBER : "))

    if choice == 1:
        #view task
        try:
            with open('todo.txt','r') as file:
                file.readline()
                if not task :
                    print("No task found!")
                else:
                    print("YOUR TODO LIST!")
                    for i, task in enumerate(i, start=1):
                        print(f'{i}.{task.strip()}')
        except FileNotFoundError:
            print(" 'todo.txt' file does not exist")

    elif choice == 2:
        # add task
        task = input("ENTER TASK: ")
        with open('todo.txt', 'a') as file:
            file.write(task + '\n')
            print('Task added', task)
    elif choice == 3:
        # delete task
        pass
    elif choice == 4:
        # exit
        # pass
        break