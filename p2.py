class Library:
    def __init__(self):
        self.books = []       # List to store book records
        self.members = []     # List to store member records
        self.book_id_counter = 1
        self.member_id_counter = 1

    # ---------- Book Operations ----------
    def add_book(self, title, author, year):
        book = {
            "id": self.book_id_counter,
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)
        self.book_id_counter += 1
        print("Book added successfully!\n")

    def list_books(self):
        if not self.books:
            print("No books available.\n")
        else:
            print("List of Books:")
            for book in self.books:
                print(f"ID: {book['id']}, Title: {book['title']}, "
                      f"Author: {book['author']}, Year: {book['year']}")
            print("")

    def update_book(self, book_id, title, author, year):
        for book in self.books:
            if book["id"] == book_id:
                book["title"] = title
                book["author"] = author
                book["year"] = year
                print("Book updated successfully!\n")
                return
        print("Book not found.\n")

    def delete_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                print("Book deleted successfully!\n")
                return
        print("Book not found.\n")

    # ---------- Member Operations ----------
    def add_member(self, name, email):
        member = {
            "id": self.member_id_counter,
            "name": name,
            "email": email
        }
        self.members.append(member)
        self.member_id_counter += 1
        print("Member added successfully!\n")

    def list_members(self):
        if not self.members:
            print("No members available.\n")
        else:
            print("List of Members:")
            for member in self.members:
                print(f"ID: {member['id']}, Name: {member['name']}, Email: {member['email']}")
            print("")

    def update_member(self, member_id, name, email):
        for member in self.members:
            if member["id"] == member_id:
                member["name"] = name
                member["email"] = email
                print("Member updated successfully!\n")
                return
        print("Member not found.\n")

    def delete_member(self, member_id):
        for member in self.members:
            if member["id"] == member_id:
                self.members.remove(member)
                print("Member deleted successfully!\n")
                return
        print("Member not found.\n")


def main():
    library = Library()

    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Add Member")
        print("6. List Members")
        print("7. Update Member")
        print("8. Delete Member")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")
            library.add_book(title, author, year)

        elif choice == "2":
            library.list_books()

        elif choice == "3":
            try:
                book_id = int(input("Enter book ID to update: "))
            except ValueError:
                print("Invalid input for book ID.\n")
                continue
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new publication year: ")
            library.update_book(book_id, title, author, year)

        elif choice == "4":
            try:
                book_id = int(input("Enter book ID to delete: "))
            except ValueError:
                print("Invalid input for book ID.\n")
                continue
            library.delete_book(book_id)

        elif choice == "5":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            library.add_member(name, email)

        elif choice == "6":
            library.list_members()

        elif choice == "7":
            try:
                member_id = int(input("Enter member ID to update: "))
            except ValueError:
                print("Invalid input for member ID.\n")
                continue
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            library.update_member(member_id, name, email)

        elif choice == "8":
            try:
                member_id = int(input("Enter member ID to delete: "))
            except ValueError:
                print("Invalid input for member ID.\n")
                continue
            library.delete_member(member_id)

        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
