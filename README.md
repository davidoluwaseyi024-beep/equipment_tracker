# Equipment Maintenance Tracker

A simple Django app for tracking equipment maintenance dates and highlighting overdue items.

## Features
- Equipment list page
- Overdue equipment page
- Django admin for data entry
- Visual overdue status badges

## Requirements
- Python 3
- Django
- SQLite

## Setup
1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies.
4. Run migrations.
5. Create a superuser.
6. Start the development server.

## Run commands
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Usage
- Open `/` for the equipment list.
- Open `/overdue/` for overdue items.
- Use `/admin/` to add equipment records.

## Screenshots
Add images to the `screenshots/` folder and reference them here.