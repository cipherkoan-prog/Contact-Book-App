# 📒 Contact Book App (CLI)

A simple command-line based Contact Book application built using Python.
This app allows you to store, search, and delete contacts using a JSON file for persistent storage.

---

## 🚀 Features

* Add new contacts
* Search contacts by name
* Delete contacts
* Data stored in a JSON file (`data.json`)
* Automatic data loading on startup

---

## 🛠️ Technologies Used

* Python
* JSON (for data storage)

---

## 📁 Project Structure

contact-book/
│
├── main.py        # Main application file
├── data.json      # Stores contact data (auto-created)
└── README.md      # Project documentation

---

## ▶️ How to Run

1. Make sure Python is installed
2. Clone or download the project
3. Open terminal in project folder
4. Run the script:

python main.py

---

## 📌 How It Works

* Contacts are stored as a list of dictionaries in `data.json`
* Each contact has:

  * name
  * phone
* Data is loaded when the app starts and saved after every change

---

## 🧠 Concepts Used

* File Handling (`open`, `read`, `write`)
* JSON Handling (`json.load`, `json.dump`)
* Lists & Dictionaries
* Functions
* Loops and Conditions

---

## 📷 Example Usage

1. Add Contact
2. Search Contact
3. Delete Contact
4. Exit

Enter your choice: 1
Enter the name: Sayan
Enter the phone number: 1234567890

---

## ⚠️ Notes

* If `data.json` does not exist, it will be created automatically
* Names are case-insensitive when searching and deleting
* Make sure not to manually corrupt the JSON file

---

## 🔮 Future Improvements

* Update contact feature
* Multiple phone numbers
* Email support
* GUI version (Tkinter or Web App)
* Sort contacts

---

## 👨‍💻 Author

Sayan Oraon

