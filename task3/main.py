import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def print_directory_structure(directory: Path, space: int = 0):
    """Рекурсивно виводить структуру директорії з colorama."""
    if not directory.exists():
        print(Fore.RED + f"Директорія {directory} не існує!")
        return

    if not directory.is_dir():
        print(Fore.RED + f"{directory} не є директорією!")
        return

    try:
        for item in sorted(directory.iterdir()):
            prefix = " " * space
            if item.is_dir():
                print(Fore.BLUE + f"{prefix}📁 {item.name}")
                print_directory_structure(item, space + 4)
            else:
                print(Fore.GREEN + f"{prefix}📄 {item.name}")
    except PermissionError:
        print(Fore.RED + f"Немає доступу до {directory.name}")


def get_directory() -> Path:
    '''Повертає шлях до директорії, яка передається як аргумент командного рядка.'''
    try:
        directory_sys = sys.argv
        if not directory_sys:
            raise FileNotFoundError
        if len(directory_sys) > 1:
            return Path(sys.argv[1]).resolve()
        elif len(directory_sys) == 1:
            return Path(sys.argv[0]).resolve().parent

    except (FileNotFoundError, NotADirectoryError) as e:
        print(Fore.RED + f"Error: {e}")

    return Path(__file__).resolve().parent

directory = get_directory()
print_directory_structure(directory)


