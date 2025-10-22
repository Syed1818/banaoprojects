Django User Authentication - Banao Task 1
This is a web application built with Python and Django for the Banao Task 1. The project implements a complete user authentication system with two distinct user roles: Patient and Doctor. It features user registration, login, and redirection to role-specific dashboards, all built with a clean, responsive Bootstrap 5 interface.
🚀 FeaturesUser Registration: A single, comprehensive signup form for both Patients and Doctors.
User Login: Secure login for registered users.
Role-Based Dashboards: Users are redirected to a unique dashboard (Patient or Doctor) upon successful login.
Profile Management: Includes profile picture uploads and detailed address fields.
Form Validation: Server-side checks for unique usernames/emails and password confirmation.
Modern UI: Built with Bootstrap 5 for a clean, responsive, and mobile-friendly experience.
Admin Panel: Full admin integration to view and manage user profiles.
🛠️ Technology StackBackend: Python, DjangoFrontend: HTML, CSS, Bootstrap 5Database: SQLite 3 (default)📸 ⚙️ Getting StartedFollow these instructions to get a copy of the project up and running on your local machine.
Prerequisites Before you begin, make sure you have Python and pip installed and refer the requirement.txt.
Installation & SetupClone the repository:
clone https://github.com/your-username/atg_project.git
cd atg_project
Create and activate a virtual environment:Bash# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install the dependencies:
Bash pip install -r requirements.txt
Apply database migrations:
Bash python manage.py makemigrations
python manage.py migrate
Create an admin superuser (optional but recommended):Bashpython manage.py createsuperuser
(Follow the prompts to create an admin username and password.)
Run the development server:
Bash python manage.py runserver
Open the application in your browser:
Login Page: http://127.0.0.1:8000/login/
Signup Page: http://127.0.0.1:8000/signup/
Admin Panel: http://127.0.0.1:8000/admin/