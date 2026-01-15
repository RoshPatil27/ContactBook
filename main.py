
# ---

# ## 📄 main.py

# ```python
from contact_book.operations import (
    add_contact,
    view_contacts,
    search_contact,
    delete_contact
)

def main():
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
