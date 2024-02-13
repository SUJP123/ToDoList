from datetime import datetime

function = 1


class Date():
    def __init__(self, name, time, educ):
        self.name = name
        self.time = time
        self.educ = educ

def run():
    tasks = [ ]
    classes = [ ]
    completed = [ ]
    while function != 0:
    ##Loop to keep app running
        start_up = "no"
        print("\n""\n" "Welcome to TO-DO List")
        print("Type 1 to add a task")
        print("Type 2 to complete/delete a task")
        print("Type 3 to view current tasks")
        print("Type 4 to view completed tasks")
        print("Type 5 to edit classes")
        print("Type 6 to view current classes""\n")
        x = int(input())
        
        match x:
            case 1:
                print("\n""Any new Tasks? yes or no" "\n")
                start_up = input()
                while start_up == 'yes':
                    print("\n""What is your new task?" "\n")
                    task = input()
                    print("\n""What date in YEAR/MM/DD format?""\n")
                    date2 = input()
                        
                    print("\n" "Would you like to organize the task to a class, yes or no?""\n")
                    cl = input()

                    if cl == "yes":
                        print("\n")
                        print(classes)
                        print("\n" "Type index of class you want to assign to""\n")
                        cl_index = int(input())
                        if cl_index not in range(len(classes)):
                            print("Given Index is not in range of classes, try inputing the task again.")
                            break
                        class1 = classes[cl_index]

                    else:
                        class1 = ''

                    obj = Date(task, date2, class1)
                    tasks.append(obj)
                    tasks.sort(key=lambda date: datetime.strptime(date.time, "%Y/%m/%d"))
                    print("\n" "Are you done adding tasks, yes or no?" "\n")
                    close = input()
                    if close == "yes":                                
                        break
                    
    
                    print("\n" f"Current TO-DO List             ")
                    for i in range(len(tasks)):
                        print("\n" f"{i+1} |{str(tasks[i].time)[:10]} {tasks[i].educ}| {tasks[i].name}|")
                        print(f"-------------------------------------------")
                        continue
            case 2:
                print("\n" f"Current TO-DO List             ")
                if len(tasks) == 0:
                    print("\n""You currently have nothing on your TO-DO List""\n")
                    break
                for i in range(len(tasks)):
                    print("\n" f"{i+1} |{str(tasks[i].time)[:10]} {tasks[i].educ}| {tasks[i].name}")
                    print(f"-------------------------------------------")
                
                print("\n" "What task would you like to complete/delete? (type task #)" "\n")
                complete_index = int(input())
                if (complete_index-1) not in range(len(tasks)):
                    print("Given Index is not in range of tasks, try inputing the task again.")
                    break
                print("\n""Would you like to add this task to completed tasks, yes or no?""\n")
                comp = input()
                if comp == 'yes':
                    completed.append(tasks[complete_index-1])
                    completed.sort()
                del tasks[complete_index-1]



            case 3:
                if len(tasks) == 0:
                    print("\n""There are currently no tasks to view.""\n")
                    break
                print("\n" f"Current TO-DO List             ")
                for i in range(len(tasks)):
                        print("\n" f"{i+1}|{str(tasks[i].time)[:10]} {tasks[i].educ}| {tasks[i].name}")
                        print(f"-------------------------------------------")
            
            case 4:
                if len(completed) == 0:
                    break
                for i in range(len(completed)):
                    print("\n" f"{i+1}|{str(completed[i].time)[:10]} {completed[i].educ}| {completed[i].name}")
                    print(f"-------------------------------------------")

            case 5:
                done = ''
                while done != 'done':
                    print("\n""Would you like to add or delete a class?""\n")
                    clinput = input()
                    if clinput == "delete":
                        if len(classes) == 0:
                            print("\n" "There are currently 0 classes to delete." "\n")
                            break
                        print(classes)
                        print("\n" "What class would you like to delete, type the index?""\n")
                        del_ind = int(input())
                        if del_ind not in range(len(classes)):
                            print("Given Index is not in range of classes, try again.")
                            break
                        del classes[(del_ind)]
                    elif clinput == "add":
                        print("\n" "What class would you like to add?""\n")
                        add_ind = input()
                        classes.append(add_ind)
                    print("\n" "Type done to finish editing classes, type no to continue editing.""\n") 
                    done = input()
            
            case 6:
                if len(classes) == 0:
                    print("\n" "There are currently 0 classes to view." "\n")
                    break
                print(" ")
                for i in range(len(classes)):
                    print(classes[i])

while __name__ == '__main__':
    run()