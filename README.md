# E-Learning Platform

A comprehensive e-learning platform built with Flask that allows instructors to create courses and students to enroll and learn.

## First Time Setup

1. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up the admin user and database:
```bash
python create_admin.py
```

This script will:
- Initialize the database
- Create necessary tables
- Set up an admin user with the following credentials:
  - Email: admin@example.com
  - Password: admin123

If you encounter any errors:
- Ensure your virtual environment is activated
- Verify all requirements are installed
- Check if the database path is writable
- Make sure your database configuration in config.py is correct

## Running the Application

1. Start the development server:
```bash
python wsgi.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Log in with the admin credentials created above.

## Features

- User authentication and authorization
- Course creation and management
- Student enrollment system
- Course content management
- Notes taking system
- Discussion forum
- Admin dashboard
- File upload support
- User profiles

## Project Structure

```
e-learning/
├── app/
│   ├── admin/         # Admin panel functionality
│   ├── auth/          # Authentication
│   ├── courses/       # Course management
│   ├── forum/         # Discussion forum
│   ├── main/          # Main routes
│   ├── notes/         # Notes functionality
│   ├── static/        # Static files
│   ├── templates/     # HTML templates
│   └── models.py      # Database models
├── migrations/        # Database migrations
├── config.py         # Configuration
├── create_admin.py   # Admin user creation
└── wsgi.py          # Application entry point
```

## Configuration

The application can be configured through environment variables or the config.py file:

- `SECRET_KEY`: Application secret key
- `DATABASE_URL`: Database connection URL (defaults to SQLite)
- `MAIL_USERNAME`: Email for notifications
- `MAIL_PASSWORD`: Email password

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
