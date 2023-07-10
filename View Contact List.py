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

# Example usage
contacts = [
    {
        'name': 'John Doe',
        'phone': '1234567890',
        'email': 'john@example.com'
    },
    {
        'name': 'Jane Smith',
        'phone': '9876543210',
        'email': 'jane@example.com'
    }
]

view_contacts(contacts)
