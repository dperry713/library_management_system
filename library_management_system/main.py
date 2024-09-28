"""
Main script for the Library Management System.
"""

import mysql.connector


# Database configuration
config = {
    'user': 'root',
    'password': 'irrelevant1',
    'host': 'localhost',
    'database': 'library_management_system',
}

# Connect to the database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def main():
    """Main function for the Library Management System."""

    while True:
        print("\nWelcome to the Library Management System with Database Integration!")
        print("****")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    """Menu for book operations."""

    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    """Adds a new book to the database."""

    title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")

    # Check if author exists, if not, add the author
    cursor.execute("SELECT id FROM authors WHERE name = %s", (author_name,))
    author_id = cursor.fetchone()
    if author_id is None:
        cursor.execute("INSERT INTO authors (name) VALUES (%s)", (author_name,))
        cnx.commit()
        author_id = cursor.lastrowid

    # Add the book to the database
    cursor.execute(
        "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)",
        (title, author_id, isbn, publication_date),
    )
    cnx.commit()
    print("Book added successfully!")

def borrow_book():
    """Allows a user to borrow a book."""

    user_id = input("Enter user ID: ")
    book_id = input("Enter book ID: ")

    # Check if the book is available
    cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
    availability = cursor.fetchone()[0]
    if not availability:
        print("Book is not available.")
        return

    # Borrow the book
    cursor.execute(
        "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())",
        (user_id, book_id),
    )
    cnx.commit()
    # Update book availability
    cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
    cnx.commit()
    print("Book borrowed successfully!")

def return_book():
    """Allows a user to return a book."""

    book_id = input("Enter book ID: ")

    # Return the book
    cursor.execute(
        "UPDATE borrowed_books SET return_date = CURDATE() WHERE book_id = %s AND return_date IS NULL",
        (book_id,),
    )
    cnx.commit()
    # Update book availability
    cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
    cnx.commit()
    print("Book returned successfully!")

def search_book():
    """Searches for a book by title or ISBN."""

    search_term = input("Enter book title or ISBN: ")

    # Search for the book
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE %s OR isbn LIKE %s",
        ("%" + search_term + "%", "%" + search_term + "%"),
    )
    books = cursor.fetchall()

    if books:
        print("\nSearch Results:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Publication Date: {book[4]}, Availability: {book[5]}")
    else:
        print("No books found matching your search criteria.")

def display_all_books():
    """Displays all books in the database."""

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if books:
        print("\nAll Books:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Publication Date: {book[4]}, Availability: {book[5]}")
    else:
        print("No books found in the database.")

def user_operations():
    """Menu for user operations."""

    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_user():
    """Adds a new user to the database."""

    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")

    # Add the user to the database
    cursor.execute(
        "INSERT INTO users (name, library_id) VALUES (%s, %s)",
        (name, library_id),
    )
    cnx.commit()
    print("User added successfully!")

def view_user_details():
    """Views details of a specific user."""

    user_id = input("Enter user ID: ")

    # Get user details
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    if user:
        print(f"\nUser Details:")
        print(f"ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")
    else:
        print("User not found.")

def display_all_users():
    """Displays all users in the database."""

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if users:
        print("\nAll Users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")
    else:
        print("No users found in the database.")

def author_operations():
    """Menu for author operations."""

    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_author():
    """Adds a new author to the database."""

    name = input("Enter author name: ")
    biography = input("Enter author biography: ")

    # Add the author to the database
    cursor.execute(
        "INSERT INTO authors (name, biography) VALUES (%s, %s)",
        (name, biography),
    )
    cnx.commit()
    print("Author added successfully!")

def view_author_details():
    """Views details of a specific author."""

    author_id = input("Enter author ID: ")

    # Get author details
    cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
    author = cursor.fetchone()

    if author:
        print(f"\nAuthor Details:")
        print(f"ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
    else:
        print("Author not found.")

def display_all_authors():
    """Displays all authors in the database."""

    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()

    if authors:
        print("\nAll Authors:")
        for author in authors:
            print(f"ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
    else:
        print("No authors found in the database.")

if __name__ == "__main__":
    main()

    # Close the database connection
    cursor.close()
    cnx.close()
