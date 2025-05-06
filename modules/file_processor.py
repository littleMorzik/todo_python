def get_todos(filepath = "todos.txt"):
    with open(filepath, "r") as file:
        todos_from_file = file.readlines()
    return todos_from_file

def save_todos(todos_to_save, filepath = "todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_to_save)