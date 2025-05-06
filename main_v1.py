from modules import file_processor
import time

curr_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", curr_time)

todos = file_processor.get_todos()

while True:
    user_action = input("Enter add, show, edit, done or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos.append(todo + "\n")
    elif user_action.startswith("show"):
        # new_todos = [item.strip("\n") for item in todos] -- list comprehension

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            todo_index = int(user_action[5:]) - 1
            new_todo = input("Enter a new todo: ") + "\n"
            todos[todo_index] = new_todo
        except ValueError:
            print('After "edit" must be number of todo')
            continue
    elif user_action.startswith("done"):
        try:
            todo_index = int(user_action[5:])
            todos.pop(todo_index - 1)
        except IndexError:
            print("There is no such amount of todos in the list")
            continue
    elif user_action.startswith("exit"):
        file_processor.save_todos(todos)
        print("Bye!")
        break
    else:
        print("Unknown command!")
