import json

CONTACT_FILE = "data/contacts.json"

def get_email(name):

    with open(CONTACT_FILE, "r") as f:

        contacts = json.load(f)

    return contacts.get(name)