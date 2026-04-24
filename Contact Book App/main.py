import json

FILE_NAME="data.json"

def load_contacts():
    try:
        with open(FILE_NAME, "r")as file:
            return json.load(file)
    except:
        return []
    
def save_contact(contact_list):
    with open(FILE_NAME,"w")as file:
        json.dump(contact_list,file,indent=4)

contact_list=load_contacts()
    
def add_contact():
    name=input("Enter the name: ")
    phone=input("Enter the phone number: ")
    contact_list.append({"name": name, "phone": phone})
    save_contact(contact_list)

def search_contact():
    name=input("Enter the name to search: ")
    for contact in contact_list:
        if contact["name"].lower() == name.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            return
    print("Contact not found.")

def delete_contact():
    name=input("Enter the name to delete: ")
    for i, contact in enumerate(contact_list):
        if contact["name"].lower()==name.lower():
            del contact_list[i]
            save_contact(contact_list)
            print("Contact deleted.")
            return
    print("Contact not found.")

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")
    
    choice=input("Enter your choice: ")
    
    if choice=="1":
        add_contact()
    elif choice=="2":
        search_contact()
    elif choice=="3":
        delete_contact()
    elif choice=="4":
        break
    else:
        print("Invalid choice. Please try again.")