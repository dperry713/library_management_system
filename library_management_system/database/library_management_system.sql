-- Create the database
CREATE DATABASE library_management_system;

-- Use the database
USE library_management_system;

-- Create the books table
CREATE TABLE books (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BIT DEFAULT 1
);

-- Create the authors table
CREATE TABLE authors (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

-- Create the users table
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

-- Create the borrowed_books table
CREATE TABLE borrowed_books (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE
);

-- Add foreign key constraints
ALTER TABLE books
ADD CONSTRAINT FK_Books_Authors FOREIGN KEY (author_id) REFERENCES authors(id);

ALTER TABLE borrowed_books
ADD CONSTRAINT FK_BorrowedBooks_Users FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE borrowed_books
ADD CONSTRAINT FK_BorrowedBooks_Books FOREIGN KEY (book_id) REFERENCES books(id);
