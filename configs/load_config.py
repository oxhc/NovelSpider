import os


def print_config(file_name):
    print(os.getcwd())
    return
    with open(file_name, 'r', encoding='utf8') as file:
        print(file.read())

if __name__ == '__main__':
    print_config("url_mapping.json")