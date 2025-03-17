from pathlib import Path
import json

from messages import ERROR_MESSAGES, MESSAGES
from found_contact import found_contact
from exceptions import ContactAlreadyExists

FILENAME = Path(__file__).parent / 'contacts.json'

def add_contact(args):
    name, phone = args
    if len(name) < 3:
        return ERROR_MESSAGES['too_short_name']
    if len(phone) <5:
        return ERROR_MESSAGES['too_short_phone']
    if not phone.isdigit() or not name.isalpha():
        return ERROR_MESSAGES['add_contact']

    new_contact = {name: phone}

    if not FILENAME.exists():
        with open(FILENAME, 'w', encoding='utf-8') as file:
            json.dump(new_contact, file, ensure_ascii=False, indent=4)
        return MESSAGES['contact_added']

    contact_exists = found_contact(name)
    if contact_exists:
        raise ContactAlreadyExists(ERROR_MESSAGES['contact_already_exists'])

    with open(FILENAME, 'r+', encoding='utf-8') as file:
        contacts = json.load(file)
        contacts[name] = phone
        file.seek(0)
        json.dump(contacts, file, ensure_ascii=False, indent=4)
        return MESSAGES['contact_added']


