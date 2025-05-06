with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    user_action = input("Enter add, show, edit, done or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
        case "show":
            # new_todos = [item.strip("\n") for item in todos] -- list comprehension

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}.{item}"
                print(row)
        case "edit":
            todo_index = int(input("Index of the todo to edit: "))
            todo_index = todo_index - 1
            new_todo = input("Enter a new todo: ") + "\n"
            todos[todo_index] = new_todo
        case "done":
            todo_index = int(input("Index of the todo to complete: "))
            todos.pop(todo_index - 1)
        case "exit":
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print("Bye!")
            break
