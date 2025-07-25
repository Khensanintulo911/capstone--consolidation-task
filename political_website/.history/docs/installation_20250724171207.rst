Installation
============

Requirements
------------

* Python 3.8+
* Django 4.0+
* Virtual environment (recommended)

Setup Instructions
------------------

1. Clone the repository::

    git clone <repository-url>
    cd political_website

2. Create and activate a virtual environment::

    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # or
    venv\Scripts\activate     # On Windows

3. Install dependencies::

    pip install -r requirements.txt

4. Run migrations::

    python manage.py migrate

5. Create a superuser::

    python manage.py createsuperuser

6. Start the development server::

    python manage.py runserver

The application will be available at http://127.0.0.1:8000/