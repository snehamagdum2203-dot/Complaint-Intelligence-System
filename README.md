# Complaint Intelligence System

## About the Project

The Complaint Intelligence System is a Python Flask web application designed to manage customer complaints efficiently. It helps users register complaints, automatically categorize them, track complaint status, and view complaint statistics through a dashboard.

This project aims to make complaint management more organized and reduce manual work.

## Features

* Register new customer complaints.
* Validate customer details and complaint information.
* Automatically categorize complaints.
* View all registered complaints.
* Update complaint status.
* Maintain a history of status changes.
* View dashboard statistics.
* Store complaint data using SQLite.
* Run automated tests using pytest.

## Complaint Categories

The system supports the following categories:

* Delivery
* Payment
* Product
* Account/Login
* Technical
* Service
* Other

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS
* pytest
* Git and GitHub

## Project Structure

```text
Complaint-Intelligence-System/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── database.py
│   ├── config.py
│   ├── validators.py
│   ├── categorizer.py
│   ├── complaint_service.py
│   ├── templates/
│   └── static/
├── database/
├── requirements.txt
├── run.py
├── setup_database.py
├── test_categorizer.py
├── test_validation.py
└── README.md
```

## Requirements

* Python 3.11 or another compatible Python version.
* pip
* A code editor such as Visual Studio Code.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/snehamagdum2203-dot/Complaint-Intelligence-System.git
```

### 2. Open the Project Folder

```bash
cd Complaint-Intelligence-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Initialize the Database

```bash
python setup_database.py
```

Run the database setup command only when initializing a new database. Check the setup script before running it if you already have complaint data, so existing data is not accidentally overwritten.

### 7. Run the Application

```bash
python run.py
```

Open the following address in your browser:

http://127.0.0.1:5000

## Running Tests

Run the automated tests with:

```bash
python -m pytest -v
```

The tests check complaint categorization and input validation.

## Future Improvements

* Add user authentication and role-based access.
* Add search and filtering options.
* Generate complaint reports.
* Improve complaint analytics.
* Deploy the application online.

## Author

Sneha Magdum

## License

This project is available for educational and portfolio purposes.
