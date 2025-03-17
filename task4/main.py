from colorama import init

from constants import MENU
from messages import ERROR_MESSAGES, MESSAGES
from add_contact import add_contact
from change_contact import change_contact
from show_phone import show_phone, show_all
from exceptions import InvalidCommand

init(autoreset=True)

def parse_input(user_input):
    if not len(user_input):
        raise InvalidCommand(ERROR_MESSAGES['bot_command'])
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    """bor for managing contacts"""
    print(MESSAGES['welcome'])
    print(MENU)
    while True:
        try:
            user_input = input(MESSAGES['enter_command'])
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(MESSAGES['bye'])
                break

            match command:
                case '1' | 'hello':
                    print(MESSAGES['greet'])
                case 'add':
                    print(add_contact(args))
                case 'change':
                    print(change_contact(args))
                case 'phone':
                    print(show_phone(args))
                case 'all':
                    print(show_all())
                case _:
                    print(ERROR_MESSAGES['command'])
                    continue
        except InvalidCommand as e:
            print(e)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

