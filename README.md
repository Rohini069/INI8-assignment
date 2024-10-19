# INI8-assignment

Software Developer Intern Assessment

Overview
This project implements a registration system with CRUD operations using Python and MySQL.

# Project Structure

- **backend/app.py**: Contains backend code and database scripts.
- **README.md**: Documentation for the project.

## Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/INI8-assignment.git
   cd INI8 assignment/backend
   ```
2. Install dependencies (if you have a requirements.txt):
   pip install -r requirements.txt
3. Run the application:
   python app.py

4. Database Setup
   Make sure to create the database and the Registration table with the following SQL in MySQL Workbench:

CREATE DATABASE rohinidb;
USE rohinidb;

CREATE TABLE Registration (
ID INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Email VARCHAR(100) NOT NULL UNIQUE,
DOB DATE NOT NULL,
PhoneNumber VARCHAR(15) NOT NULL
);
