import json
import os

#file to store contact data
CONTACTS_FILE = 'contacts.txt'

def load_contacts():
    """Load contact data from the file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    """Save contact data to the file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts List:")
    for name, info in contacts.items():
        print(f"{name}: Phone: {info['phone']}, Email: {info['email']}")
    print()

def edit_contact(contacts):
    """Edit an Existing Contact."""
    name = input("Enter name of the contact to edit: ")
    if name in contacts:
        print(f"Editing contact: {name}")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ")
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    """Main function to interact with the contact management system."""
    contacts = load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Manager. ")
            break
        else:
            print("Invalid Choice. Please Try Again.")

if __name__=="__main__":
    main()