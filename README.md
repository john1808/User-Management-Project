# User Management System

## Setup
```bash
git clone <repo-url>
cd user_mgmt
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints
- POST `/api/accounts/register/` → Register user
- POST `/api/token/` → Login (JWT)
- GET `/api/accounts/profile/` → View profile
- PUT `/api/accounts/profile/` → Update profile
- POST `/api/accounts/reset-password/` → Reset password
- CRUD `/api/tasks/` → Tasks operations
