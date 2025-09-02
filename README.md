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



## Database Setup

```sql
CREATE DATABASE user_mgmt_db;
CREATE USER user_mgmt_user WITH PASSWORD 'password@123';
ALTER ROLE user_mgmt_user SET client_encoding TO 'utf8';
ALTER ROLE user_mgmt_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE user_mgmt_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE user_mgmt_db TO user_mgmt_user;


```markdown
Update `settings.py` DATABASES section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'user_mgmt_db',
        'USER': 'user_mgmt_user',
        'PASSWORD': 'password@123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
