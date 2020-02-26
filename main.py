# Case-study #7
# Developers:   Drachev Nikita (),
#               Starnovskiy Sergey (),
#               Zhuravlev Alexander ()
import os
import local_en as lc

lang = input(lc.INPUT)
while lang != '2' and lang != '1':
    print(lc.ERROR)
    lang = input(lc.INPUT)
if lang == '1':
    import local_en as lc
else:
    import local_ru as lc


# TODO: write functions: main(), accept_command(),run_command() - Sergey


def main():
    while True:
        print(os.getcwd())
        print(lc.MENU)
        command = accept_command()


def accept_command():
    command = input(lc.CHOICE)
    while command != '1' and command != '2' and command != '3' and command != '4' and command != '5' and \
            command != '6' and command != '7':
        print(lc.ERROR_1)
        command = input(lc.CHOICE)
    if command == '1':
        return 'open_dir'
    elif command == '2':
        return 'move_up'
    elif command == '3':
        return 'move_down'
    elif command == '4':
        return 'count_files'
    elif command == '5':
        return 'count_bytes'
    elif command == '6':
        return 'find_files'
    elif command == '7':
        return 'exit'


def open_dir():
    return


# TODO: write functions: move_up(), move_down(currentDir), count_files(path) - Alexander

def move_up():
    return


def move_down():
    return


def count_files():
    return


# TODO: write functions: count_bytes(path), find_files(target, path) - Nikita

def count_bytes(path):
    return


def find_files(target, path):
    return
