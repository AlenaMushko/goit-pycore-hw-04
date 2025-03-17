from colorama import Fore, init

init(autoreset=True)

ERROR_MESSAGES = {
    "bot_command": f"{Fore.RED}Command can't be empty.",
    "command": f"{Fore.RED}Invalid command!",
    "too_short_name": f"{Fore.RED}Name is too short. Please enter more than 3 characters.",
    "too_short_phone": f"{Fore.RED}Phone is too short. Please enter more than 5 characters.",
    'add_contact': f"{Fore.RED}Please enter name and phone number in following format: <name><phone>",
    "contact_already_exists": f"{Fore.RED}This contact already exist.",
    "invalid_json": f"{Fore.RED}Invalid JSON format.",
    "no_contact": f"{Fore.RED}No contact found.",
}

MESSAGES = {
    "welcome": f"{Fore.LIGHTCYAN_EX}Welcome to the assistant bot!",
    "enter_command": f"{Fore.CYAN}Enter your choice: {Fore.RESET}",
    'greet': f"{Fore.YELLOW}How can I help you?",
    "bye": f"{Fore.YELLOW}Good bye!",
    "contact_added": f"{Fore.GREEN}Contact added.",
    "contact_changed": f"{Fore.GREEN}Contact updated.",
    "contacts_empty": f"{Fore.YELLOW}There are no contacts exists.",
}
