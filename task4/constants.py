from colorama import Fore, init

init(autoreset=True)

MENU = f"""
{Fore.RESET}        Commands menu:
{Fore.CYAN}#1 - Say hello to the assistant      {Fore.RESET}(type: "hello")
{Fore.GREEN}#2 - Add a new contact               {Fore.RESET}(type: "add <username> <phone>")
{Fore.YELLOW}#3 - Update an existing contact      {Fore.RESET}(type: "change <username> <phone>")
{Fore.BLUE}#4 - Find a contact's phone number   {Fore.RESET}(type: "phone <username>")
{Fore.MAGENTA}#5 - Show all saved contacts         {Fore.RESET}(type: "all")
{Fore.RED}#6 - Exit the assistant              {Fore.RESET}(type: "exit" or "close")
"""
