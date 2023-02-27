# Django Online Learning Platform

This is a web-based platform built on Django that allows users to create and participate in online courses. The platform allows course creators to upload and organize course materials such as videos, quizzes, and assignments, while students can enroll in courses and track their progress.


# Features

* User authentication and registration system
* Course creation and management
* Course enrollment and progress tracking
* Upload and organization of course materials
* User dashboard to track enrolled courses and progress
* Search functionality to find courses
* Responsive design for mobile and desktop devices
* Admin panel for site management

# Installation

Clone the repository to your local machine:

` git clone https://github.com/your-username/online-learning-platform.git `

# Navigate to the project directory:

`cd online-learning-platform`

# Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate

```
# Install the project dependencies:

`pip install -r requirements.txt`

# Run database migrations:

`python manage.py migrate`


# Create a superuser account:

`python manage.py createsuperuser`

# Start the development server:

`python manage.py runserver`

# Usage

Once the development server is running, you can access the site by navigating to `http://localhost:8000/` in your web browser.

To create a new course, log in as a superuser and navigate to the admin panel. From there, you can create new courses and add materials such as videos, quizzes, and assignments.

Students can enroll in courses by navigating to the course page and clicking the "Enroll" button. They can then access the course materials and track their progress.










