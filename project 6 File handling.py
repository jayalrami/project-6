from datetime import datetime

FILENAME = "journal.txt"

def add_entry():
    entry = input("Write your journal entry: ")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, "a") as file:
        file.write(f"[{time}] {entry}\n")

    print("Entry added successfully!")

def view_entries():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No journal entries found.")
            return

        print("\nJournal Entries:")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")

    except FileNotFoundError:
        print("Journal file not found.")

def search_entries():
    try:
        keyword = input("Enter keyword: ").lower()

        with open(FILENAME, "r") as file:
            lines = file.readlines()

        found = False
        for line in lines:
            if keyword in line.lower():
                print(line.strip())
                found = True

        if not found:
            print("No matching entries found.")

    except FileNotFoundError:
        print("Journal file not found.")

def delete_entries():
    confirm = input("Delete all entries? (yes/no): ").lower()
    if confirm == "yes":
        open(FILENAME, "w").close()
        print("All entries deleted.")
    else:
        print("Delete cancelled.")

# Main Program
print("Welcome to Personal Journal Manager")

while True:
    print("\n1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("User input: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        delete_entries()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
