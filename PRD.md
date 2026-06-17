# PRD: Carros Inventory Management System

**Goal:** Provide a web-based platform for managing vehicle inventory and user authentication.

## Core Features
1. **User Authentication:** Registration and login functionality managed by the `accounts` app.
2. **Car Management:** Create, Read, Update, Delete (CRUD) operations for vehicle listings, handled by the `cars` app.
3. **Inventory Tracking:** Model-based tracking of car attributes (brand, plate, photo, biography).

## Tech Stack
- **Framework:** Django 5.2.5
- **Database:** SQLite (dev), supports PostgreSQL (via `psycopg2`).
- **Templating:** Django Templates.
- **Deployment:** uWSGI.
- **Integrations:** OpenAI API client initialized (`openai_api/client.py`).

## Constraints
- Must maintain compatibility with existing `cars` and `accounts` Django app structures.
- Deployment environment expects `uwsgi` configuration.
