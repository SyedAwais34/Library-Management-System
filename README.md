# 📚 Library Management System

A Python-based Library Management System that allows students to create accounts, borrow and return books, manage wallet balance, and lets admins manage books and users.  
The project uses JSON files for data storage and follows Object-Oriented Programming concepts.

---

# 🚀 Features

## 👨‍🎓 Student Features

✅ Create Account  
✅ Login System  
✅ View All Books  
✅ Borrow Books  
✅ Return Books  
✅ Wallet Balance System  
✅ Fine Calculation for Late Returns  
✅ Update Account Details  
✅ Delete Account  

---

## 👨‍💼 Admin Features

✅ Admin Login  
✅ Add Books  
✅ Delete Books  
✅ Update Books  
✅ View All Books  
✅ View All Users  

---

# 🛠️ Technologies Used

- Python
- JSON
- OOP (Object-Oriented Programming)
- File Handling
- Datetime Module

---

# 📂 Project Structure

```bash
library-management-system/
│
├── main.py
├── data.json
├── books.json
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/library-management-system.git
```

## 2️⃣ Open Project Folder

```bash
cd library-management-system
```

## 3️⃣ Run the Program

```bash
python main.py
```

---

# 📖 Main Menu

```text
==== Library Management System ====

Press 1 to create account
Press 2 to login as student
Press 3 to login as admin
Press 4 to exit
```

---

# 👨‍💼 Admin Credentials

```text
Email: admin@gmail.com
Password: 1234
```

---

# 💾 Data Storage

## Student Data

Stored inside:

```bash
data.json
```

Example:

```json
[
  {
    "name": "Awais",
    "age": 20,
    "email": "awais@gmail.com",
    "password": "password123",
    "accountNo.": "A1b@23",
    "balance": 500,
    "borrow_book": []
  }
]
```

---

## Books Data

Stored inside:

```bash
books.json
```

Example:

```json
[
  {
    "book_id": 1,
    "book_name": "Python Basics",
    "book_author": "John Doe",
    "book_price": 50,
    "book_quantity": 10
  }
]
```

---

# 🔐 Security Features

- Unique Account Number Generation
- Password Validation
- Admin Authentication
- Balance Verification
- Fine Calculation for Late Returns

---

# 📌 Concepts Used

This project demonstrates:

- Classes & Objects
- Class Methods
- File Handling
- JSON Data Storage
- Datetime Operations
- Input Validation
- List Comprehension
- Random ID Generation

---

# 🧠 Future Improvements

- GUI Version using Tkinter
- Database Integration (MySQL/MongoDB)
- Password Encryption
- Search Books Feature
- Email Notifications
- Transaction History
- Book Reservation System

---

# 👨‍💻 Author

Muhammad Awais

Instagram: @codingwithawais

---

# ⭐ GitHub

If you like this project, give it a ⭐ on GitHub!
