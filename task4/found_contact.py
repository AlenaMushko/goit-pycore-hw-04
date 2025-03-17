from pathlib import Path
import json
from messages import ERROR_MESSAGES

FILENAME = Path(__file__).parent / 'contacts.json'

def found_contact(name: str) -> dict | None:
    if not FILENAME.exists():
        return None
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            contacts = json.load(file)
            if not isinstance(contacts, dict):
                print(ERROR_MESSAGES['invalid_json'])
                return None

            for dict_name, phone in contacts.items():
                if dict_name.lower() == name.lower():
                    return {dict_name: phone}

    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
