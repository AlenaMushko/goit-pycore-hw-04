from pathlib import Path
import json

from messages import ERROR_MESSAGES, MESSAGES
from found_contact import found_contact
from exceptions import NoFoundContact

FILENAME = Path(__file__).parent / 'contacts.json'

def change_contact(args):
    name, phone = args
    if len(name) < 3:
        return ERROR_MESSAGES['too_short_name']
    if len(phone) <5:
        return ERROR_MESSAGES['too_short_phone']
    if not phone.isdigit() or not name.isalpha():
        return ERROR_MESSAGES['add_contact']

    contact_exists = found_contact(name)
    if not contact_exists:
        raise NoFoundContact(ERROR_MESSAGES['no_contact'])

    try:
        with open(FILENAME, 'r+', encoding='utf-8') as file:
            contacts = json.load(file)
            for old_name, old_phone in contacts.items():
                if old_name.lower() == name.lower():
                    contacts[old_name] = phone
                    break

            file.seek(0)
            json.dump(contacts, file, ensure_ascii=False, indent=4)
            return MESSAGES['contact_changed']

    except json.JSONDecodeError:
        return ERROR_MESSAGES['invalid_json']
    except Exception as e:
        return e

