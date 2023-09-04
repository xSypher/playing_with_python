#Script in python that allows me to add, delete and consult contacts.

import os

#Contact class to makes them easy.
class Contact:
    def __init__(self, name='', age=0, 
                email='', address=0):
        
        self._name = name
        self._age = age 
        self._email = email
        self._addres = address

    def __str__(self):
        return f"""    
    *-------------------------------------------------
    | Name: {self._name}                              
    |------------------------------------------------- 
    | Age: {self._age}                                
    |-------------------------------------------------
    | Email: {self._email}                             
    |-------------------------------------------------
    | Addres: {self._addres}                          
    *-------------------------------------------------
"""

    def change_name(self,chng):
        self._name = chng

    def change_age(self, chng):
        self._age = chng
        
    def change_email(self, chng):
        self._email = chng

    def change_addres(self, chng):
        self._address = chng


#---------------------Program main functions----------------
data_base = {} #Data base for save the contacts information

def clear_screen():
    os.system('clear')

def interface():
    while True: #loop for user decisions.
        clear_screen()
        print("""     Menu.      

1) Add a conctact.
2) Delete a contact.
3) Consult contacts.
4) Exit.
""")

        try: 
            opc = int(input("Select an option: "))
            if opc == 1:
                clear_screen()
                add_contact()
            elif opc == 2:
                clear_screen() 
                delete_contact()
            elif opc == 3:
                clear_screen()
                consult_contacts()
            elif opc == 4:
                break
        except ValueError:
            input("That was an invalid option, please try again.")

def add_contact():
    while True:
        clear_screen()
        try:
            name = input("Name: ")
            age = int(input("Age: "))
            email = input("Email: ")
            address = input("Address: ")
            break
        except ValueError:
            input("Invalid character, please put a corresponding character.")
    contact = Contact(name, age, email, address)
    if name in data_base:
        name = data_base[name]
        contact_number = len(name)+1
        name[contact_number] = contact
    else:
        data_base[name] = {1: contact}
    
    clear_screen()
    print(contact)
    input("Contact added successfully. Press enter to continue...")

def delete_contact():
    if len(data_base) > 0:
        while True:
            clear_screen()
            name = input(f"Write the name of the contact, (write exit to return to the menu.): ")
            if name in data_base:
                clear_screen()
                for k, v in data_base[name].items():
                    print(f"Contact number: {k}")
                    print(v)
                print("There are more than one contact with that name.")
                while True:
                    contact_to_delete = int(input("Choose the number of contact to delete: "))
                    try:
                        data_base[name].pop(contact_to_delete)
                        input("The contact was deleted successfully. Press enter to continue...")
                        break
                    except KeyError:
                        print("Invalid option. Try again.")
            elif name.lower() == "exit":
                break      
            
            else:
                input("There's no contact with that name.")
    input("There are no contacts to delete...")

def consult_contacts():
    if len(data_base) > 0:
        clear_screen()
        for name, contacts in data_base.items():
            for contact in contacts.values():
                print(name[0].upper())
                print(contact) 
        input("Press enter to continue...")
    input("There are no contacts to consult...")
def main():
    interface()

if __name__ == "__main__":
    main()


     









    
