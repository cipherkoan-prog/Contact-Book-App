# 📒 Contact Book App (CLI)

A simple yet robust command-line Contact Book application built with Python. The application allows users to manage contacts efficiently by adding, searching, updating, and deleting records. All contact information is stored in a JSON file, ensuring data is preserved between program runs.

---

## ✨ Features

- ➕ Add new contacts
- 🔍 Search contacts by name (case-insensitive)
- ✏️ Update existing contact phone numbers
- 🗑️ Delete contacts
- 💾 Automatic JSON data storage
- 📂 Automatically loads saved contacts on startup
- 🚫 Prevents duplicate contact names
- ✅ Validates phone numbers (numeric and 10 digits)
- ⚠️ Handles missing or invalid JSON files gracefully
- 🧹 Removes leading and trailing spaces from user input

---

## 🛠️ Technologies Used

- Python 3
- JSON (Data Storage)

---

## 📁 Project Structure

```text
contact-book/
│
├── main.py         # Main application
├── data.json       # Stores contact data (auto-created)
└── README.md       # Project documentation
```

---

## ▶️ How to Run

### Prerequisites

- Python 3.x installed on your system

### Steps

1. Clone this repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd contact-book
```

3. Run the application:

```bash
python main.py
```

---

## 📋 Menu Options

```text
1. Add Contact
2. Search Contact
3. Delete Contact
4. Update Contact
5. Exit
```

---

## 📌 How It Works

- Contacts are stored as dictionaries inside a list.
- All data is saved in `data.json`.
- Existing contacts are automatically loaded when the application starts.
- Every change is immediately saved to the JSON file.

Example contact format:

```json
{
    "name": "Sayan",
    "phone": "9876543210"
}
```

---

## 🧠 Concepts Demonstrated

This project demonstrates the use of:

- Functions
- File Handling
- JSON Serialization (`json.load`, `json.dump`)
- Lists & Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- Input Validation
- CRUD Operations (Create, Read, Update, Delete)

---

## 📷 Example Usage

```text
1. Add Contact
2. Search Contact
3. Delete Contact
4. Update Contact
5. Exit

Enter your choice: 1

Enter the name: Sayan
Enter the phone number: 9876543210

Contact added successfully.
```

---

## ⚠️ Error Handling

The application safely handles:

- Missing `data.json` file
- Empty or invalid JSON files
- Empty names
- Duplicate contacts
- Invalid phone numbers
- Updating with the same phone number
- Searching or deleting non-existent contacts

---

## 🚀 Future Improvements

- 📞 Multiple phone numbers per contact
- 📧 Email address support
- ⭐ Favorite contacts
- 🔤 Display contacts in alphabetical order
- 📋 View all contacts option
- 🖥️ Tkinter GUI version
- 🏗️ Object-Oriented Programming (OOP) version
- 🔍 Search by phone number

---

## 🌱 What I Learned

While building this project, I learned:

- Working with JSON files for persistent storage
- Implementing CRUD operations
- Writing modular code using functions
- Validating user input
- Handling exceptions gracefully
- Improving program reliability through error handling

---

## 🎯 Project Status

✅ Completed

---

## 👨‍💻 Author

**Sayan Oraon**

---

## 📄 License

This project is created for learning and educational purposes.
