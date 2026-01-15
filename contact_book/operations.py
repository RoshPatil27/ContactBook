from contact_book.storage import contacts
from utils.helpers import format_contact

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- CONTACT LIST ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {format_contact(contact)}")

def search_contact():
    search_name = input("Enter name to search: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == search_name:
            print("Contact found:")
            print(format_contact(contact))
            return

    print("Contact not found.")

def delete_contact():
    name_to_delete = input("Enter name to delete: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name_to_delete:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")
