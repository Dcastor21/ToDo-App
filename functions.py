FILEPATH= "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and returns the list of
    to-do items"""
    with open(filepath, 'r') as file_local:
        reader = file_local.readlines()

    return reader


def write_todos(todos_arg, filepath= FILEPATH):
    """ Write the to-dos items list in the text file"""
    with open(filepath, 'w') as file_writer:
        writer = file_writer.writelines(todos_arg)