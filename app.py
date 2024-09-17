def task():
    tasks=[]
    print("-----WELCOME EO THE TASK MANAGEMENT--------")
    total_task=int (input("Enter how many taska you want to add="))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task{i}")
        tasks.append(task_name)
    print(f"Today's taska are\n{tasks}")
    
    while True:
        try:
            operation=int(input("Enter \n1-Add\n2Updae\n3Delete\n-View\n5-Exit/stop\n"))
            if operation ==1:
                add = input("Enter task you want to add=")
                task.append(add)
            elif operation == 2:
                updated_val=input("Enter the task name you want to update =")
                if updated_val in tasks:
                    up=input ("Enter new task=")
                    ind=task.index(updated_val)
                    tasks[ind]=up
                    print (f"Updated task'{updated_val}to {up}")
                else:
                    print("Task not found.")
            elif operation ==3:
                del_val = input ("which task you want to delete=")
                if del_val in tasks:
                    ind=tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task'{del_val}'has been deleted.")
                else:
                    print("Task not found")
            elif operation == 4:
                print(f"Total task={tasks}")
                break
            else:
                print("INVALID INPUT")
        except ValueError:
            print ("Invalid Input .please enter a valid number.")
  
task()                  
                
                    
                    