from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def total_salary(path: Path) -> tuple[int, float] | tuple[None, None]:
    """Returns the total and average salary."""
    try:
        path = Path(path)
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) == 0:
                raise ValueError(f"{Fore.RED}File is empty")

            salaries = []
            for line in lines:
                try:
                    salary = int(line.split(',')[1])
                    salaries.append(salary)
                except ValueError:
                    print(f"{Fore.RED}Invalid value: {line.strip()}")

            total = sum(salaries)
            average = round(total / len(salaries), 2)
            return total, average

    except FileNotFoundError:
        print(f'{Fore.RED}File not found')
    except ValueError as e:
        print(f'{Fore.RED}{e}')
    except Exception as e:
        print(f'{Fore.RED}Something went wrong: {e}')

    return None, None

total, average = total_salary("employees.txt")
print(f"{Fore.GREEN} {'Загальна сума заробітної плати:'} {Fore.YELLOW}{total} {Fore.GREEN}{', Середня заробітна плата:'} {Fore.YELLOW}{average}")
