# Simple contact book using Python

print("Welcome to the Contact Book".center(50))

# Global contact dictionary
my_dict = {}

# Function to add a contact
def add_contact():
    name = input("Enter contact Name = ")
    number = input("Enter contact Number = ")
    if name in my_dict:
        print("Contact already exists .. ")
    elif number in my_dict.values():
        print("Number already exists .. ")
    else:
        my_dict[name] = number
        print("Contact added successfully ... ")

# Function to search a contact
def search_contact():
    print("Choose the below options to search : ")
    print("1. Search by Name ")
    print("2. Search by Number")
    print("3. Exit to main menu ")

    choice = int(input("Enter your choice :: "))

    if choice == 1:
        name = input("Enter the name to search :: ")
        if name in my_dict:
            print(f"Contact found: {name} - {my_dict[name]}")
        else:
            print("Contact not found .. ")
    elif choice == 2:
        number = input("Enter the number to search :: ")
        found = False
        for name, num in my_dict.items():
            if num == number:
                print(f"Contact found: {name} - {number}")
                found = True
                break
        if not found:
            print("Contact not found .. ")
    elif choice == 3:
        return
    else:
        print("Invalid choice .. ")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete contact :: ")
    if name in my_dict:
        del my_dict[name]
        print("Contact deleted successfully .. ")
    else:
        print("Contact not found .. ")

# Function to display all contacts
def display_contacts():
    if my_dict:
        print("All contacts:")
        for name, number in my_dict.items():
            print(f"Name: {name}".ljust(20), f"Number: {number}".rjust(20))
    else:
        print("No contacts found.")

# Main loop
def contact_book():
    while True:
        print("\nHere are commands to use the contact book :: ")
        print("1. Add a contact ")
        print("2. Search a contact ")
        print("3. Delete a contact ")
        print("4. Display all contacts ")
        print("5. Exit ")
        a = int(input("Enter your choice :: "))
        if a == 1:
            add_contact()
        elif a == 2:
            search_contact()
        elif a == 3:
            delete_contact()
        elif a == 4:
            display_contacts()
        elif a == 5:
            print("Exiting the contact book .. ")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
contact_book()
