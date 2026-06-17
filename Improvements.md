# Potential Improvements

- **Testing Coverage:** Existing `tests.py` in `cars` and `accounts` are minimal/empty. Implement unit and integration tests using `pytest` for better reliability.
- **Environment Management:** Currently `DEBUG = True` and hardcoded `SECRET_KEY` exist in `settings.py`. Transition to environment variables using `python-dotenv` or `dj-database-url`.
- **Static/Media Handling:** Use a dedicated cloud storage service (e.g., AWS S3) for production media and static files instead of local file system paths.
- **CI/CD:** Add a CI pipeline (e.g., GitHub Actions) to run tests and linters automatically on pull requests.
- **Code Quality:** Integrate `black` or `ruff` for automated code formatting and linting.
