"""
To-do List Application

- user input, variable & strings
- Lists, sets
- Loops & Conditions
- Functions & f-strings

"""
tasks = []
completed_task = set()


# add a task
def add_task():
  "Add a new task to the task list"
  task = input("please enter the new task here->")
  tasks.append(task)
  print(f"<{task}> added successfully to the task list.\n")

# view the tasks
def view_task():
    "view all the task"
    if not tasks:
        print("No tasks available to display.\n")
        return
    print("\n***** TO-DO List *****")
    for idx, task in enumerate(tasks, start=1):
        status = "completed" if task in completed_task else "Pending"
        print(f"{idx}. {task} - {status}")

# marks task as completed
def mark_completed(task_number):
    "Mark a task as completed using its number."
    if 1 <= task_number <= len(tasks):
        task_item = tasks[task_number-1]
        completed_task.add(task_item)
        print(f"Task ->> {task_item} << marked as completed.\n")
    else:
        print("Invalid task number.\n")



# delete a task
def delete_task(task_number):
    "Delete a task from the list using its number."
    if 1 <= task_number <= len(tasks):
        task_item = tasks.pop(task_number-1)
        completed_task.discard(task_item)
        print(f"Task >>{task_item} << delete successfully.\n")
    else:
        print("Invalid task numer.\n")   

def main():
    while True:
        print("""\n ==== To-Do List App ====\n      1. Add Task\n      2. View Task\n      3. Mark Task as completed\n      4. Delete Task\n      5. Exit\n      """)
        choice = input("Enter your choice(1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            try:
                task_no = int(input("Enter the task number to mark completed->"))
                mark_completed(task_no)
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "4":
            try:
                task_no = int(input("Enter the task number to delete ->"))
                delete_task(task_no)
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "5":
            print("Exiting To-Do app. Goodbye!\n")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()



