import uuid
from datetime import datetime, timedelta
import csv

# Book Class #
# Represents a book with all its attributes
class Book:
    def __init__(self, title, author, year, publisher, num_copies, publication_date):
        self.book_id = str(uuid.uuid4())  # Unique book ID
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.num_copies = num_copies
        self.publication_date = publication_date

    # Setters for book attributes
    def set_title(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError("Title must be a string")

    def set_author(self, author):
        if isinstance(author, str):
            self.author = author
        else:
            raise ValueError("Author must be a string")

    def set_year(self, year):
        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError("Year must be an integer")

    def set_publisher(self, publisher):
        if isinstance(publisher, str):
            self.publisher = publisher
        else:
            raise ValueError("Publisher must be a string")

    def set_num_copies(self, num_copies):
        if isinstance(num_copies, int) and num_copies >= 0:
            self.num_copies = num_copies
        else:
            raise ValueError("Number of copies must be a non-negative integer")

    def set_publication_date(self, publication_date):
        if isinstance(publication_date, str):
            self.publication_date = publication_date
        else:
            raise ValueError("Publication date must be a string in format YYYY-MM-DD")

    # Getters for book attributes
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_num_copies(self):
        return self.num_copies

    def get_publication_date(self):
        return self.publication_date

# BookList Class #
# Manages a collection of Book objects
class BookList:
    def __init__(self):
        self.books = {}  # Dictionary to store books by book_id
        self.load_books_from_csv()  # Load books from CSV on initialization

    # Load books data from CSV into the books dictionary
    def load_books_from_csv(self):
        try:
            with open('7.9- Assessment 2/MinaLibraryBooks.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        title=row['title'], author=row['author'], year=int(row['year']),
                        publisher=row['publisher'], num_copies=int(row['num_copies']),
                        publication_date=row['publication_date']
                    )
                    book.book_id = row['book_id']
                    self.books[book.book_id] = book
                print("Books loaded from MinaLibraryBooks.csv")
        except FileNotFoundError:
            print("MinaLibraryBooks.csv not found. Starting with an empty book list.")

    # Save current book data to CSV
    def save_books_to_csv(self):
        with open('7.9- Assessment 2/MinaLibraryBooks.csv', mode='w', newline='') as file:
            fieldnames = ['book_id', 'title', 'author', 'year', 'publisher', 'num_copies', 'publication_date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books.values():
                writer.writerow({
                    'book_id': book.book_id,
                    'title': book.title,
                    'author': book.author,
                    'year': book.year,
                    'publisher': book.publisher,
                    'num_copies': book.num_copies,
                    'publication_date': book.publication_date
                })
            print("Books have been saved to MinaLibraryBooks.csv")

    # Add a new book to the collection
    def add_book(self, book):
        if book.book_id not in self.books:
            self.books[book.book_id] = book
            print(f"Book added: {book.title}, by {book.author}")
            self.save_books_to_csv()
        else:
            raise ValueError("Book with this ID already exists")

    # Search for a book by title, author, publisher, or publication date
    def search_book(self, title=None, author=None, publisher=None, publication_date=None):
        results = []
        for book in self.books.values():
            if (title and book.title == title) or \
                    (author and book.author == author) or \
                    (publisher and book.publisher == publisher) or \
                    (publication_date and book.publication_date == publication_date):
                results.append(book)
        return results

    # Modify a book's attributes by its ID
    def modify_book(self, book_id, title=None, author=None, year=None, publisher=None, num_copies=None):
        if book_id in self.books:
            book = self.books[book_id]
            if title:
                book.set_title(title)
            if author:
                book.set_author(author)
            if year:
                book.set_year(year)
            if publisher:
                book.set_publisher(publisher)
            if num_copies is not None:
                book.set_num_copies(num_copies)
            print("Book details updated successfully.")
            self.save_books_to_csv()
        else:
            raise ValueError("Book ID not found")

    # Return all books as a list, useful for displaying books in the CLI
    def list_books(self):
        return self.books.values()

# User Class #
# Represents a library user with various personal attributes
class User:
    def __init__(self, username, first_name, surname, house_number, street_name, postcode, email, date_of_birth):
        self.username = username
        self.first_name = first_name
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.date_of_birth = date_of_birth

    # Setters for user attributes
    def set_first_name(self, first_name):
        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            raise ValueError("First name must be a string")

    def set_surname(self, surname):
        if isinstance(surname, str):
            self.surname = surname
        else:
            raise ValueError("Surname must be a string")

    def set_house_number(self, house_number):
        if isinstance(house_number, str):
            self.house_number = house_number
        else:
            raise ValueError("House number must be a string")

    def set_street_name(self, street_name):
        if isinstance(street_name, str):
            self.street_name = street_name
        else:
            raise ValueError("Street name must be a string")

    def set_postcode(self, postcode):
        if isinstance(postcode, str):
            self.postcode = postcode
        else:
            raise ValueError("Postcode must be a string")

    def set_email(self, email):
        if isinstance(email, str):
            self.email = email
        else:
            raise ValueError("Email must be a string")

    # Getters for user attributes
    def get_username(self):
        return self.username

    def get_first_name(self):
        return self.first_name

    def get_surname(self):
        return self.surname

# UserList Class #
# Manages a collection of User objects
class UserList:
    def __init__(self):
        self.users = {}
        self.load_users_from_csv()  # Load user data from CSV on initialization

    # Load user data from CSV into the users dictionary
    def load_users_from_csv(self):
        try:
            with open('7.9- Assessment 2/MinaLibraryUsers.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(
                        username=row['username'], first_name=row['first_name'], surname=row['surname'],
                        house_number=row['house_number'], street_name=row['street_name'], postcode=row['postcode'],
                        email=row['email'], date_of_birth=row['date_of_birth']
                    )
                    self.users[user.username] = user
                print("Users loaded from MinaLibraryUsers.csv")
        except FileNotFoundError:
            print("MinaLibraryUsers.csv not found. Starting with an empty user list.")

    # Method to retrieve user by username
    def get_user_by_username(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise ValueError("User not found")

    # Save user data to CSV
    def save_users_to_csv(self):
        with open('7.9- Assessment 2/MinaLibraryUsers.csv', mode='w', newline='') as file:
            fieldnames = ['username', 'first_name', 'surname', 'house_number', 'street_name', 'postcode', 'email', 'date_of_birth']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users.values():
                writer.writerow({
                    'username': user.username,
                    'first_name': user.first_name,
                    'surname': user.surname,
                    'house_number': user.house_number,
                    'street_name': user.street_name,
                    'postcode': user.postcode,
                    'email': user.email,
                    'date_of_birth': user.date_of_birth
                })
            print("Users have been saved to MinaLibraryUsers.csv")

    # Add a new user to the collection
    def add_user(self, user):
        if user.username not in self.users:
            self.users[user.username] = user
            print(f"User added: {user.username}")
            self.save_users_to_csv()
        else:
            raise ValueError("User with this username already exists")

    # Modify user details
    def modify_user(self, username, first_name=None, surname=None, house_number=None, street_name=None, postcode=None, email=None):
        if username in self.users:
            user = self.users[username]
            if first_name:
                user.set_first_name(first_name)
            if surname:
                user.set_surname(surname)
            if house_number:
                user.set_house_number(house_number)
            if street_name:
                user.set_street_name(street_name)
            if postcode:
                user.set_postcode(postcode)
            if email:
                user.set_email(email)
            print("User details updated successfully.")
            self.save_users_to_csv()
        else:
            raise ValueError("Username not found")

    # List all users, useful for displaying users in the CLI
    def list_users(self):
        return self.users.values()

# Loan Class #
# Manages loan transactions and keeps track of borrowed books
class Loan:
    def __init__(self):
        self.loans = []
        self.load_loans_from_csv()  # Load loans from CSV on initialization

    # Load loan data from CSV
    def load_loans_from_csv(self):
        try:
            with open('7.9- Assessment 2/MinaLibraryLoans.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = row['user_username']
                    book_id = row['book_id']
                    due_date = datetime.strptime(row['due_date'], '%Y-%m-%d')
                    self.loans.append({'user': user, 'book_id': book_id, 'due_date': due_date})
                print("Loans loaded from MinaLibraryLoans.csv")
        except FileNotFoundError:
            print("MinaLibraryLoans.csv not found. Starting with an empty loans list.")

    # Save loan data to CSV
    def save_loans_to_csv(self):
        with open('7.9- Assessment 2/MinaLibraryLoans.csv', mode='w', newline='') as file:
            fieldnames = ['user_username', 'book_id', 'due_date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for loan in self.loans:
                writer.writerow({
                    'user_username': loan['user'],
                    'book_id': loan['book_id'],
                    'due_date': loan['due_date'].strftime('%Y-%m-%d')
                })
            print("Loans have been saved to MinaLibraryLoans.csv")

    # Record a new book loan
    def borrow_book(self, user, book, duration):
        if book.num_copies > 0:
            due_date = datetime.now() + timedelta(days=duration)
            self.loans.append({'user': user.username, 'book_id': book.book_id, 'due_date': due_date})
            book.set_num_copies(book.num_copies - 1)
            print(f"Book borrowed: {book.title} by {user.username}, due on {due_date.strftime('%Y-%m-%d')}")
            self.save_loans_to_csv()
        else:
            raise ValueError("Book not available for borrowing")

    # Return a borrowed book
    def return_book(self, user, book):
        for loan in self.loans:
            if loan['user'] == user.username and loan['book_id'] == book.book_id:
                self.loans.remove(loan)
                book.set_num_copies(book.num_copies + 1)
                print(f"Book returned: {book.title} by {user.username}")
                self.save_loans_to_csv()
                return
        raise ValueError("Loan record not found")

    # List all overdue books
    def list_overdue_books(self):
        overdue_books = []
        current_date = datetime.now()
        for loan in self.loans:
            if loan['due_date'] < current_date:
                overdue_books.append((loan['book_id'], loan['user']))
        return overdue_books

    # List all loaned books (for display)
    def list_loans(self):
        return self.loans

# CLI for managing library system
def main():
    booklist = BookList()
    userlist = UserList()
    loan_system = Loan()

    while True:
        print("\nWelcome to Mina's Awesome Library Management System!")
        print("1. Add a new book to the library collection.")
        print("2. Are you new here? Register as a user.")
        print("3. Want to borrow a book? Key in your details and pick a book.")
        print("4. Need to return a borrowed book? Let us help with that.")
        print("5. Search for a book or edit an existing one.")
        print("6. Modify user details.")
        print("7. Check if any books are overdue.")
        print("8. Show all users.")
        print("9. Show all books.")
        print("10. Show all books currently out.")
        print("11. Exit the system.")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                # Add a new book
                title = input("Enter book title: ").strip()
                author = input("Enter author: ").strip()
                year = int(input("Enter publication year: ").strip())
                publisher = input("Enter publisher: ").strip()
                num_copies = int(input("Enter number of copies: ").strip())
                publication_date = input("Enter publication date (YYYY-MM-DD): ").strip()
                book = Book(title, author, year, publisher, num_copies, publication_date)
                booklist.add_book(book)
                print("Book added successfully!")

            elif choice == "2":
                # Register as a new user
                username = input("Enter username: ").strip()
                first_name = input("Enter first name: ").strip()
                surname = input("Enter surname: ").strip()
                house_number = input("Enter house number: ").strip()
                street_name = input("Enter street name: ").strip()
                postcode = input("Enter postcode: ").strip()
                email = input("Enter email: ").strip()
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ").strip()
                user = User(username, first_name, surname, house_number, street_name, postcode, email, date_of_birth)
                userlist.add_user(user)
                print("User registered successfully!")

            elif choice == "3":
                # Borrow a book
                username = input("Enter your username: ").strip()
                user = userlist.get_user_by_username(username)
                book_title = input("Enter the book title you want to borrow: ").strip()
                book = next((b for b in booklist.books.values() if b.title == book_title), None)
                if book is None:
                    raise ValueError("Book not found")
                duration = int(input("Enter borrowing duration (in days): ").strip())
                loan_system.borrow_book(user, book, duration)
                print(f"Book '{book_title}' borrowed successfully for {duration} days.")

            elif choice == "4":
                # Return a borrowed book
                username = input("Enter your username: ").strip()
                user = userlist.get_user_by_username(username)
                book_title = input("Enter the book title you want to return: ").strip()
                book = next((b for b in booklist.books.values() if b.title == book_title), None)
                if book is None:
                    raise ValueError("Book not found")
                loan_system.return_book(user, book)
                print(f"Book '{book_title}' returned successfully.")

            elif choice == "5":
                # Search or modify a book
                sub_choice = input("Enter 's' to search for a book or 'm' to modify an existing book: ").strip().lower()
                if sub_choice == 's':
                    # Search for a book
                    title = input("Enter title to search (or leave blank): ").strip()
                    author = input("Enter author to search (or leave blank): ").strip()
                    publisher = input("Enter publisher to search (or leave blank): ").strip()
                    publication_date = input("Enter publication date to search (or leave blank, format YYYY-MM-DD): ").strip()
                    results = booklist.search_book(title, author, publisher, publication_date)
                    if results:
                        print("Books found:")
                        for book in results:
                            print(f"- {book.title} by {book.author}")
                    else:
                        print("No books found with the given criteria.")
                elif sub_choice == 'm':
                    # Modify a book
                    book_id = input("Enter the book ID to modify: ").strip()
                    title = input("Enter new title (or leave blank to keep current): ").strip()
                    author = input("Enter new author (or leave blank to keep current): ").strip()
                    year = input("Enter new year (or leave blank to keep current): ").strip()
                    publisher = input("Enter new publisher (or leave blank to keep current): ").strip()
                    num_copies = input("Enter new number of copies (or leave blank to keep current): ").strip()
                    booklist.modify_book(
                        book_id,
                        title=title if title else None,
                        author=author if author else None,
                        year=int(year) if year else None,
                        publisher=publisher if publisher else None,
                        num_copies=int(num_copies) if num_copies else None,
                    )

            elif choice == "6":
                # Modify user details
                username = input("Enter the username to modify: ").strip()
                first_name = input("Enter new first name (or leave blank to keep current): ").strip()
                surname = input("Enter new surname (or leave blank to keep current): ").strip()
                house_number = input("Enter new house number (or leave blank to keep current): ").strip()
                street_name = input("Enter new street name (or leave blank to keep current): ").strip()
                postcode = input("Enter new postcode (or leave blank to keep current): ").strip()
                email = input("Enter new email (or leave blank to keep current): ").strip()
                userlist.modify_user(
                    username,
                    first_name=first_name if first_name else None,
                    surname=surname if surname else None,
                    house_number=house_number if house_number else None,
                    street_name=street_name if street_name else None,
                    postcode=postcode if postcode else None,
                    email=email if email else None,
                )

            elif choice == "7":
                # List overdue books
                overdue_books = loan_system.list_overdue_books()
                if overdue_books:
                    print("Overdue books:")
                    for book_id, username in overdue_books:
                        print(f"- Book ID: {book_id} borrowed by {username}")
                else:
                    print("No overdue books at the moment.")

            elif choice == "8":
                # Show all users
                print("All users:")
                for user in userlist.list_users():
                    print(f"{user.get_username()}")

            elif choice == "9":
                # Show all books
                print("All books:")
                for book in booklist.list_books():
                    print(f"{book.get_title()} by {book.get_author()}")

            elif choice == "10":
                # Show all books currently on loan
                print("All books currently on loan:")
                for loan in loan_system.list_loans():
                    print(f"Book ID: {loan['book_id']} borrowed by {loan['user']}")

            elif choice == "11":
                # Exit
                print("Thank you for using Mina's Awesome Library Management System! Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
