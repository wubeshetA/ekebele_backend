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

1. Create a PostgreSQL database on your local machine.
2. Create a new `.env` file in the root directory of the project.
3. Copy the content of `.env.example` into the newly created `.env` file.
4. Update the database configuration in the `.env` file with your local PostgreSQL database details.

## Usage

### Running the Development Server

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