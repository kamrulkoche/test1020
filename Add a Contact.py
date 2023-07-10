def add_contact():
    contacts = []  # List to store contacts
    
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

# Example usage
contacts = add_contact()
print(contacts)
