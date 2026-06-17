# OpenCode Instructions for Carros Project

- **Development Commands:**
  - Run development server: `python manage.py runserver`
  - Run database migrations: `python manage.py migrate`
  - Create migrations: `python manage.py makemigrations`
  - Running tests: `python manage.py test`

- **Architecture:**
  - Standard Django structure.
  - Apps: `cars` (car inventory management), `accounts` (user auth).
  - Settings: `app/settings.py`.
  - Templates: Located in `cars/templates/` and `app/templates/`.
  - Media: Uploaded files stored in `/media/`.

- **Operational Gotchas:**
  - Development environment uses `db.sqlite3`.
  - Deployment uses `uwsgi` via `carros_uwsgi.ini`.
  - If packages are missing, ensure virtual environment is active: `source .venv/bin/activate` (or equivalent).
