                             # To do list 
         
def add_task(tasks):
      
   task_name = input("\nEnter the task to add in your list :")
   if task_name:
      tasks.append({"task_name":task_name,"done":False})
      print("\nTask Added")
   else:
      print("Task cannot be empty")

def view_task(tasks):
    if not  tasks:
       print("No Task in Your To Do List till now ! ") 
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = " ✔️ " if task["done"] else "❌"
            print(f"{i}. [{status}] {task['task_name']}")
        print()

def  mark_task(tasks):
   
   try:
        index = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("\nTask marked as done.")
        else:
            print("Invalid task number.")
   except ValueError:
        print("Please enter a valid number.")
   
def delete_task(tasks):
   view_task(tasks)
   try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['task_name']}")
        else:
            print("Invalid task number.")
   except ValueError:
        print("Please enter a valid number.")

def display_menu():
    tasks =[]

    while True:
     print("="*30)
     print("\n Welcome in To Do List ")
     print("1.Add a Task")
     print("2.View all Task")
     print("3.Mark  a Task as complete")
     print("4.Delete  a Task")
     print("5.Exit")

     choice  = input("Enter your choice (1-5)")
     if choice == '1':
        add_task(tasks)
     elif choice == '2':
        view_task(tasks)
     elif choice == '3':
        mark_task(tasks)
     elif choice == '4':
        delete_task(tasks)
     elif choice== '5':
        print("\nThank you ! for using !")
        break
     else:
        print("Please choose a valid choice! ")

if __name__=="__main__":
   display_menu()



