FILEPATH="todos.txt"


def get_todos(filepath=FILEPATH):
    """Read text file and returns a list of 
    to-do-items.
    """
    with open(filepath,"r") as file_local:
        todos_local=file_local.readlines()
    return todos_local


def write_todos(todos_args,filepath=FILEPATH):
    """Write the todo item list in the text file."""
    with open(filepath,"w") as file_local:
        file_local.writelines(todos_args)

if __name__== "__main__":
    print("Hello")
    print(get_todos())