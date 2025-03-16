import random

from faker import Faker

def create_mock_data(file_name: str, num_records:int) -> None:
    """Creates mock data with random names and salaries."""
    f= Faker()
    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(num_records):
            salary = random.randint(1000, 10000)
            record = f'{f.name()},{salary}\n'
            file.write(record)

if __name__ == '__main__':
    create_mock_data('employees.txt', 10)
