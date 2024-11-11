# eKebele Backend

This is the backend service for the eKebele project. It provides APIs for managing various functionalities of the eKebele system.

## Requirements

- Python 3.11.1 or above
- Virtual environment tool (e.g., `venv`)
- PostgreSQL database

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/wubeshetA/ekebele_backend.git
cd ekebele_backend
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

- On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Set Up PostgreSQL Database

#### Install PostgreSQL Client

- On Windows:
    1. Download and install PostgreSQL from the [official PostgreSQL website](https://www.postgresql.org/download/windows/).
    2. During installation, make sure to select the option to install `psql` (SQL Shell).

- On macOS:
    1. Install PostgreSQL using Homebrew:
        ```bash
        brew install postgresql
        ```

- On Linux:
    1. Install PostgreSQL using your package manager. For example, on Ubuntu:
        ```bash
        sudo apt update
        sudo apt install postgresql postgresql-contrib
        ```

#### Creating a PostgreSQL Database

- On Windows:
    1. Open the SQL Shell (psql) from the Start menu.
    2. Connect to your PostgreSQL server by entering your server details.
    3. Create a new database by running the following command:
        ```sql
        CREATE DATABASE ekebele_db;
        ```

- On macOS and Linux:
    1. Open your terminal.
    2. Switch to the PostgreSQL user:
        ```bash
        sudo -i -u postgres
        ```
    3. Open the PostgreSQL prompt:
        ```bash
        psql
        ```
    4. Create a new database by running the following command:
        ```sql
        CREATE DATABASE ekebele_db;
        ```
    5. Exit the PostgreSQL prompt:
        ```sql
        \q
        ```
    6. Exit the PostgreSQL user:
        ```bash
        exit
        ```

2. Create a new `.env` file in the root directory of the project.
3. Copy the content of `.env.example` into the newly created `.env` file.
4. Update the database configuration in the `.env` file with your local PostgreSQL database details.

## Usage

### Running the Development Server

First, run the database migration.
```bash
python manage.py migrate
```
Then, run the development server
```bash
python manage.py runserver
```

### Running Tests

```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request
