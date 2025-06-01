import os

TODO_FILE = "todos.txt"

def load_todos():
    """Loads todo items from the file."""
    todos = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            for line in f:
                todos.append(line.strip())
    return todos

def save_todos(todos):
    """Saves todo items to the file."""
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(todo + "\n")

def add_todo(todo_item, todos):
    """Adds a new todo item."""
    todos.append(f"[ ] {todo_item}")
    print(f"Added: '{todo_item}'")

def list_todos(todos):
    """Lists all todo items."""
    if not todos:
        print("No todos yet! Add some tasks to get started.")
        return

    print("\n--- Your Todo List ---")
    for i, todo in enumerate(todos):
        print(f"{i + 1}. {todo}")
    print("----------------------")

def complete_todo(index, todos):
    """Marks a todo item as complete."""
    if 0 <= index < len(todos):
        if "[ ]" in todos[index]:
            todos[index] = todos[index].replace("[ ]", "[x]", 1)
            print(f"Completed: '{todos[index].split(' ', 1)[1]}'")
        else:
            print("This task is already marked as complete.")
    else:
        print("Invalid todo number.")

def delete_todo(index, todos):
    """Deletes a todo item."""
    if 0 <= index < len(todos):
        deleted_item = todos.pop(index)
        print(f"Deleted: '{deleted_item.split(' ', 1)[1]}'")
    else:
        print("Invalid todo number.")

def display_menu():
    """Displays the main menu options."""
    print("\n--- Todo CLI Menu ---")
    print("1. Add a new todo")
    print("2. List all todos")
    print("3. Mark todo as complete")
    print("4. Delete a todo")
    print("5. Exit")
    print("---------------------")

def main():
    """Main function to run the todo CLI."""
    todos = load_todos()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the todo item: ")
            add_todo(item, todos)
        elif choice == '2':
            list_todos(todos)
        elif choice == '3':
            try:
                list_todos(todos)
                index = int(input("Enter the number of the todo to complete: ")) - 1
                complete_todo(index, todos)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                list_todos(todos)
                index = int(input("Enter the number of the todo to delete: ")) - 1
                delete_todo(index, todos)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            save_todos(todos)
            print("Goodbye! Your todos have been saved.")
            break
        else:
            print("Invalid choice. Please try again.")
        save_todos(todos) # Save after each operation for persistence

if __name__ == "__main__":
    main()
