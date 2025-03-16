from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def get_cats_info(path: Path) -> list[dict]:
    """Reads cats info from file and returns list of dicts."""
    try:
        path = Path(path)
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) == 0:
                raise ValueError(f"{Fore.RED}File is empty")

            cats_info = []
            for line in lines:
                try:
                    id, name, age = line.strip().split(',')
                    cats_info.append({ 'id': id, 'name': name, 'age': int(age)})
                except ValueError:
                    print(f"{Fore.RED}Invalid value: {line.strip()}")
            return cats_info

    except FileNotFoundError:
        print(f'{Fore.RED}File not found')
    except ValueError as e:
        print(f'{Fore.RED}{e}')
    except Exception as e:
        print(f'{Fore.RED}Something went wrong: {e}')

        return []


cats_info = get_cats_info("cats_info.txt")
print(cats_info)
