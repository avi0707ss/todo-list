class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.id}. {self.description} [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print("Task marked as completed.")
                return
        print("Task not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new description: ")
            todo_list.update_task(task_id, new_description)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.mark_task_completed(task_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
