FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Reads a list of to-do items
    :param filepath: filename to read todos list from
    :return: list of todos items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Saves a list of to-do items to a file
    :param todos_arg: list of to-do items
    :param filepath: filename to write a list
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
