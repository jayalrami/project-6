📔 Personal Journal Manager (Python)

A simple command-line journal application written in Python that allows users to write, view, search, and delete personal journal entries stored in a text file.

🚀 Features

✍️ Add journal entries with automatic timestamps

📖 View all saved journal entries

🔍 Search entries by keyword (case-insensitive)

🗑️ Delete all journal entries with confirmation

💾 Data stored locally in a text file (journal.txt)

🛠️ Technologies Used

Python 3

Built-in modules:

datetime

File handling (open, read, write)

📂 Project Structure
journal_manager/
│
├── journal.py        # Main Python program
├── journal.txt       # Journal entries (auto-created)
└── README.md         # Project documentation

▶️ How to Run

Make sure Python 3 is installed on your system.

Save the code in a file named journal.py.

Open a terminal or command prompt in the project directory.

Run the program:

python journal.py

📋 Menu Options

When the program runs, you will see the following menu:

1. Add Entry
2. View Entries
3. Search Entries
4. Delete All Entries
5. Exit

1️⃣ Add Entry

Write a new journal entry.
Each entry is saved with a timestamp.

2️⃣ View Entries

Displays all journal entries in chronological order.

3️⃣ Search Entries

Search for entries containing a specific keyword.

4️⃣ Delete All Entries

Deletes all journal entries after confirmation.

5️⃣ Exit

Closes the program safely.

🧠 Example Entry Format
[2025-01-01 14:32:10] Had a productive day learning Python.

⚠️ Notes

If journal.txt does not exist, it will be created automatically.

Deleting entries cannot be undone.

The program runs entirely in the terminal.

🌱 Future Improvements (Optional)

Delete individual entries

Password protection

Save entries using JSON or a database

Export entries to another file

Add categories or moods
