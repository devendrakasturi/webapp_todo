def count(phrase):
    return phrase.count('.')


def get_todos(filepath="files/todos_fun.txt"):
    with open(filepath) as file:
        todos_fun = file.readlines()
    return todos_fun


def write_todos(todos_local, filepath="files/todos_fun.txt"):
    print('Inside 1st write todos')
    with open(filepath, "w") as file:
        file.writelines(todos_local)


def write_todos(todos_local, filepath="files/todos_fun.txt", mode="w"):
    print('Inside 2nd write todos')
    with open(filepath, mode) as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print("Hello in if condition")
