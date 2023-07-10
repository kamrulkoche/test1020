import sys

def add_contact(contacts):
    id = input("Enter the ID: ")
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    contact = {
        'id': id,
        'name': name,
        'phone': phone,
        'email': email
    }
    
    contacts.append(contact)
    print("Contact added successfully!")
    print("-----------------------")
    
    return contacts


def view_contacts(contacts):
    if len(contacts) == 0:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for contact in contacts:
            print("ID:", contact['id'])
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("-----------------------")


def search_contacts(contacts, query):
    matched_contacts = []
    
    for contact in contacts:
        ##if query.lower() in contact['id'or 'name'].lower():
         if query.lower() == contact['id'].lower() or search_query.lower() in contact['name'].lower() or search_query.lower() in contact['phone'].lower():
            matched_contacts.append(contact)
    
    return matched_contacts


def delete_contact(contacts, id):
    deleted = False
    
    for contact in contacts:
        if contact['id'].lower() == id.lower():
            contacts.remove(contact)
            deleted = True
            break
    
    if deleted:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
    
    return contacts


def edit_contact(contacts, id):
    edited = False
    
    for contact in contacts:
        if contact['id'].lower() == id.lower():
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email address: ")
            
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            edited = True
            break
    
    if edited:
        print("Contact edited successfully!")
    else:
        print("Contact not found.")
    
    return contacts


# Example usage

contacts = []  # Empty contact list

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
         n = int(input("Enter the number of contacts you want to add: "))

# Add n contacts
         for _ in range(n):
          contacts = add_contact(contacts)
        
    elif choice == '2':
        view_contacts(contacts)
    elif choice == '3':
        search_query = input("Enter a id or partial name or phone to search: ")
        matched_contacts = search_contacts(contacts, search_query)

        if len(matched_contacts) == 0:
            print("No contacts found.")
        else:
            print("Matching contacts:")
            for contact in matched_contacts:
                print("ID:", contact['id'])
                print("Name:", contact['name'])
                print("Phone:", contact['phone'])
                print("Email:", contact['email'])
                print("-----------------------")
    elif choice == '4':
        delete_id = input("Enter the id of the contact to delete: ")
        contacts = delete_contact(contacts, delete_id)
    elif choice == '5':
        edit_id = input("Enter the id of the contact to edit: ")
        contacts = edit_contact(contacts, edit_id)
    elif choice == '6':
        print("Exiting the program...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
