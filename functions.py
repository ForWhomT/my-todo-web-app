def get_todos(filepath="todos.txt"): # The given filename is a default, used unless a new argument is passed
    """ THIS IS A DOC STRING - Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """ THIS IS A DOC STRING - Write the to-do list to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
#This part only prints when the funtion program itself is ran, not when it is imported into another program