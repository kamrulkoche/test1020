def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    
    contacts.append(contact)
    print("Contact added successfully!")
    
    return contacts


def view_contacts(contacts):
    if len(contacts) == 0:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for contact in contacts:
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("-----------------------")


def search_contacts(contacts, query):
    matched_contacts = []
    
    for contact in contacts:
        if query.lower() in contact['name'].lower():
            matched_contacts.append(contact)
    
    return matched_contacts


def delete_contact(contacts, name):
    deleted = False
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            deleted = True
            break
    
    if deleted:
        print("Contact deleted successfully!")
        view_contacts(contacts)
    else:
        print("Contact not found.")
    
    return contacts



def edit_contact(contacts, name):
    edited = False
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email address: ")
            
            contact['phone'] = new_phone
            contact['email'] = new_email
            edited = True
            break
    
    if edited:
        print("Contact edited successfully!")
        view_contacts(contacts)
    else:
        print("Contact not found.")
    
    return contacts




# Example usage

contacts = []  # Empty contact list

n = int(input("Enter the number of contacts you want to add: "))

for _ in range(n):
    contacts = add_contact(contacts)

# View contact list
view_contacts(contacts)

# Search contacts
search_query = input("Enter a name to search: ")
matched_contacts = search_contacts(contacts, search_query)

if len(matched_contacts) == 0:
    print("No contacts found.")
else:
    print("Matching contacts:")
    for contact in matched_contacts:
        print("Name:", contact['name'])
        print("Phone:", contact['phone'])
        print("Email:", contact['email'])
        print("-----------------------")

# Delete a contact
delete_name = input("Enter the name of the contact to delete: ")
contacts = delete_contact(contacts, delete_name)

# Edit a contact
edit_name = input("Enter the name of the contact to edit: ")
contacts = edit_contact(contacts, edit_name)