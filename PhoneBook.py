from os import system
from time import sleep
import json


# FUNCTIONS
# Update the data file
def update_json_file(dic):
    with open('phone_book.json', 'w') as update_file:
        json.dump(dic, update_file)


# Get user action
def get_action():
    while True:
        print("\n\tWelcome to your PhoneBook")
        # Menu
        print('\n\tPlease choose an action :\n\n\t1-Add a new contact\n\t2-Delete an exist contact\n\t3-Search by '
              'name\n\t4-Search by '
              'phone number\n\t5-Change a number\n\t6-Change a name')
        # Show exist contacts
        show_phonebook(dictionary)
        chosen = input("\n\tPlease select a number from above : ")
        if not chosen.isnumeric():
            print('\tinvalid input try again : ')
            sleep(1.5)
            system('cls')
            continue
        elif int(chosen) < 1 or int(chosen) > 7:
            print('\tinvalid input try again : ')
            sleep(1.5)
            system('cls')
            continue
        else:
            return chosen


# Add a new contact
def add_new_contact(dic):
    print('\n\t********** Add a new contact **********')
    while True:
        name = input("\n\tPlease insert a Name : ").capitalize()
        if len(name) == 0:
            print('\tYou have not entered the name of the new contact Please try again')
            continue
        number = input("\n\tPlease insert a Number : ")
        if not number.isnumeric() or len(number) == 0:
            print('\tYou have not entered the NUMBER Please try again')
            continue
        # Create a new contact
        new_contact = {'name': name, 'number': number}
        # Add new contact to list
        dic.append(new_contact)
        return dic


# Show exist contacts
def show_phonebook(dic):
    print('\n\t********************')
    for contact in dic:
        print(f"\t{contact['name']} : {contact['number']}")
    print('\t********************')


# Delete an exist contact
def delete_contact(dic):
    print('\n\t********** Delete an exist contact **********')
    name = input("\n\tPlease insert a name to DELETE : ").capitalize()
    if len(name) == 0:
        print(f'\n\tPlease insert a name')
    for contact in dic:
        if contact['name'] == name:
            dic.remove(contact)
            print(f'\n\t**{name}** removed successfully')
            return dic
    print("\n\tnot found")
    return dic


# Clear screen
def clear_screen():
    input("\n\tPlease enter a key for Continue...")
    system("cls")


# Search contact by number
def search_by_number(dic):
    print('\n\t********** Search contact by number **********')
    number = input('\n\tInsert the number : ')
    # Search for contact
    for contact in dic:
        if contact['number'] == number:
            print(f'\n\t**{contact['number']}** is phone number of **{contact['name']}**')
            return
    print('\n\tNot found')


# Search contact by name
def search_by_name(dic):
    print('\n\t********** Search contact by name **********')
    name = input('\n\tInsert the name : ').capitalize()
    # Search for contact
    for contact in dic:
        if contact['name'] == name:
            print(f'\n\t**{contact['number']}** is phone number of **{contact['name']}**')
            return
    print("\n\tnot found")


# Change number of an exist contact
def change_number(dic):
    print('\n\t********** Change the number of an exist contact **********')
    name = input('\n\tInsert the name : ').capitalize()
    for contact in dic:
        if contact['name'] == name:
            new_number = input('\n\tInsert the new number : ')
            if not new_number.isnumeric() or len(new_number) == 0:
                print('\tYou have not entered the NUMBER Please try again')
                return dic
            # Change the number
            contact['number'] = new_number
            print(f'\n\t{name} Updated')
            print(f'\n\t**{contact['number']}** is phone number of **{contact['name']}**')
            return dic
    print("\n\tnot found")
    return dic


# Change the name of an exist contact
def change_name(dic):
    print('\n\t********** Change the name of an exist contact **********')
    while True:
        name = input('\n\tInsert the name : ').capitalize()
        for contact in dic:
            if contact['name'] == name:
                new_name = input('\n\tInsert the new name : ').capitalize()
                if len(new_name) == 0:
                    print('\tYou have not entered the name of the new contact Please try again')
                    return dic
                # Change the name
                contact['name'] = new_name
                return dic
        print("\n\tnot found")
        return dic


# Read the data file
with open('phone_book.json', 'r') as file:
    dictionary = json.load(file)

# Run app
while True:
    item = get_action()
    if item == "1":
        dictionary = add_new_contact(dictionary)
        update_json_file(dictionary)
        clear_screen()
    elif item == "2":
        dictionary = delete_contact(dictionary)
        update_json_file(dictionary)
        clear_screen()
    elif item == "3":
        search_by_name(dictionary)
        clear_screen()
    elif item == "4":
        search_by_number(dictionary)
        clear_screen()
    elif item == "5":
        dictionary = change_number(dictionary)
        update_json_file(dictionary)
        clear_screen()
    elif item == "6":
        dictionary = change_name(dictionary)
        update_json_file(dictionary)
        clear_screen()
    else:
        print("\n\tPlease select a valid number")
        continue
