# Library Management System Database

This SQL script defines the database schema for a simple library management system.

## Tables

The database consists of the following tables:

* **books:** Stores information about books in the library.
    * `id`: Unique identifier for each book.
    * `title`: Title of the book.
    * `author_id`: Foreign key referencing the `authors` table.
    * `isbn`: ISBN number of the book.
    * `publication_date`: Date of publication.
    * `availability`: Flag indicating whether the book is currently available for borrowing (1 for available, 0 for unavailable).
* **authors:** Stores information about authors.
    * `id`: Unique identifier for each author.
    * `name`: Name of the author.
    * `biography`: Brief biography of the author.
* **users:** Stores information about library users.
    * `id`: Unique identifier for each user.
    * `name`: Name of the user.
    * `library_id`: Unique library ID assigned to the user.
* **borrowed_books:** Tracks borrowed books.
    * `id`: Unique identifier for each borrowed book record.
    * `user_id`: Foreign key referencing the `users` table.
    * `book_id`: Foreign key referencing the `books` table.
    * `borrow_date`: Date when the book was borrowed.
    * `return_date`: Date when the book was returned (NULL if the book is still borrowed).

## Foreign Keys

The database uses foreign keys to establish relationships between tables:

* `books` table has a foreign key constraint on `author_id` referencing the `authors` table.
* `borrowed_books` table has foreign key constraints on `user_id` referencing the `users` table and `book_id` referencing the `books` table.

## Usage

This SQL script can be used to create the database schema for a library management system. You can execute the script in your preferred database management system to create the tables and relationships.

## Notes

* The `availability` column in the `books` table can be used to track whether a book is currently available for borrowing.
* The `return_date` column in the `borrowed_books` table can be used to track when a borrowed book was returned.
* You can add more columns to the tables as needed to accommodate additional information.
