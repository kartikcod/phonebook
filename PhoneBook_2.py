class Phonebook:
    def __init__(self):
        self.contacts ={}

    def add_contact (self, name, phone, email ) :
        self.contacts[name] ={'phone':phone, 'email':email}
        print("contact for added  successfully")

    def view_contacts (self) :
        if not self.contacts:
            print("NO contacts available")

        else:
            for name, details in self.contacts.items():
                print(f"Name:{name}")
                print(f"Phone:{details['phone']}")
                print(f"Email:{details['email']}")


    def search_contact (self, name):
        if name in self.contacts:
            print(f"found contact for {name}")
            print(f"phone:{self.contacts[name]['Phone']}")
            print(f"Email:{self.contacts[name]['Email']}")
        else:
            print(f"No Contact not found for {name}")

    def delete_contact (self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"contact for {name} deleted successfully")

        else:
            print(f"No contact found for {name} ")

def main():
    phonebook = Phonebook()

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice =='1':
            name=input("Enter name: ")
            phone=input("Enter Phone Number: ")
            email=input("Enter email: ")
            phonebook.add_contact(name, phone, email)

        elif choice =='2':
            phonebook.view_contacts()

        elif choice =='3':
            name=input("Enter name to search: ")
            phonebook.search_contact(name)

        elif choice =='4':
            name=input("Enter name to delete: ")
            phonebook.delete_contact(name)

        elif choice =='5':
            print("Exiting phonebook")
            break

        else:
            print("Invalid choice, please try again")




if __name__ == "__main__":
    main()



