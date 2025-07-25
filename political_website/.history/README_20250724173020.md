# Political Candidate Website

A Django-based web application that provides a platform for political candidates to showcase their profiles, engage with voters, and manage their online presence.

## 🚀 Features

- **Candidate Profile Management** - Create and manage detailed candidate profiles
- **User Authentication & Registration** - Secure login system for users and candidates
- **Contact Form** - Allows voters to send feedback and inquiries
- **Administrative Interface** - Django admin panel for content management
- **Responsive Design** - Mobile-friendly interface
- **Documentation** - Comprehensive Sphinx documentation

## 📋 Requirements

- Python 3.8+
- Django 4.0+
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Khensanintulo911/capstone--consolidation-task.git
   cd capstone--consolidation-task
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
political_website/
├── candidate/              # Candidate app
├── contact/                # Contact form app
├── user_auth/              # User authentication app
├── political_candidate_website/  # Main Django project
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── docs/                   # Sphinx documentation
├── requirements.txt        # Python dependencies
└── manage.py              # Django management script
```

## 🏗️ Apps Overview

### Candidate App
- Handles candidate profiles and authentication
- Views: `profile`, `login_view`, `logout_view`

### Contact App
- Manages contact form functionality
- Views: `send_feedback`

### User Auth App
- User registration and authentication
- Views: `register`

## 🌐 URL Routes

- `/` - Home page
- `/welcome/` - Welcome page
- `/profile/` - Candidate profile
- `/login/` - Candidate login
- `/logout/` - Candidate logout
- `/register/` - User registration
- `/contact/` - Contact form
- `/admin/` - Django admin interface

## 📚 Documentation

The project includes comprehensive Sphinx documentation. To build and view the documentation:

1. **Navigate to the docs directory:**
   ```bash
   cd docs
   ```

2. **Build the documentation:**
   ```bash
   make html
   ```

3. **View the documentation:**
   ```bash
   open _build/html/index.html
   ```

## 🧪 Testing

Run the test suite with:
```bash
python manage.py test
```

## 🚀 Deployment

### Development
The project is configured for development with Django's built-in server. For production deployment, consider:

- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up a reverse proxy (Nginx)
- Configuring environment variables for sensitive settings
- Using a production database (PostgreSQL, MySQL)

### Environment Variables
Create a `.env` file in the project root for sensitive configurations:
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Khensani Daniel Ntulo**
- GitHub: [@Khensanintulo911](https://github.com/Khensanintulo911)

## 📞 Support

If you have any questions or need help with the project, please:

1. Check the [documentation](docs/)
2. Open an issue on GitHub
3. Contact the development team

## 🔄 Version History

- **v0.0.1** - Initial release
  - Basic candidate profile functionality
  - User authentication system
  - Contact form implementation
  - Administrative interface

---

*Built with ❤️ using Django*