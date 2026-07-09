import json

FILE_NAME="data.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r")as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_contact(contact_list):
    with open(FILE_NAME,"w")as file:
        json.dump(contact_list,file,indent=4)

contact_list=load_contacts()
    
def add_contact():

    name = input("Enter the name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        phone = input("Enter the phone number: ").strip()

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("phone number must be numeric and 10-digits.")
    except ValueError:
        print("Invalid phone number. Please enter a valid numeric and 10-digit phone number.")
        return

    
    for contact in contact_list:
        if contact["name"].lower() == name.lower():
            print("Contact already exists.")
            return
    

    contact_list.append({"name": name, "phone": phone})
    save_contact(contact_list)
    print("Contact added successfully.")

def search_contact():

    name = input("Enter the name to search: ").strip()

    if not name:
        print("Name cannot be empty.")
        return
    
    for contact in contact_list:
        if contact["name"].lower() == name.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            return
    print("Contact not found.")

def delete_contact():
    
    name = input("Enter the name to delete: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    for i, contact in enumerate(contact_list):
        if contact["name"].lower()==name.lower():
            del contact_list[i]
            save_contact(contact_list)
            print("Contact deleted.")
            return
    print("Contact not found.")

def update_contact():
    
    name = input("Enter the name to update: ").strip()

    if not name:
        print("Name cannot be empty.")
        return
    for contact in contact_list:
        if contact["name"].lower() == name.lower():
            new_phone = input("Enter the new phone number: ").strip()
            if not new_phone.isdigit() or len(new_phone) != 10:
                print("Invalid phone number. Please enter a valid numeric and 10-digit phone number.")
                return
            if contact["phone"] == new_phone:
                print("New phone number is the same as the current one.")
                return
            contact["phone"] = new_phone
            save_contact(contact_list)
            print("Contact updated.")
            return
    print("Contact not found.")

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Exit")
    
    choice=input("Enter your choice: ")
    
    if choice=="1":
        add_contact()
    elif choice=="2":
        search_contact()
    elif choice=="3":
        delete_contact()
    elif choice=="4":
        update_contact()
    elif choice=="5":
        break
    else:
        print("Invalid choice. Please try again.")