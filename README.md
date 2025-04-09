LearnEarn Project

Contains Django-based LearnEarn project files, including models, views, templates, and static assets.

📚 LearnEarn – Learning Management System (LMS)

Deployed on: (https://www.pythonanywhere.com)
Tech Stack: Django 4.x | Python 3.x | HTML5 | CSS3 | Bootstrap | PostgreSQL/MySQL (if applicable)

🚀 Project Overview
LearnEarn is a Django-based Learning Management System that allows learners to browse courses, access course materials (files, videos, quizzes), and request enrolment. Admins can manage courses, approve/reject learner requests, and send email notifications.

🔥 Key Features

🟡 User Authentication: Secure signup, login, and logout.
🎓 Course Management:
Admin: Add, update, and delete courses.
Learners: Enrol in courses, access files, videos, and quizzes.
✉ Email Notifications: Automatic emails for course approval/rejection.
🏢 Company Management: Store and display company details.
📩 File & Video Uploads: Course-specific resources with download/view options.
🛠 Installation & Setup

1️⃣ Clone the Repository

git clone cd LearnEarn projects

2️⃣ Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
pip install -r requirements.txt

3️⃣ Apply Migrations & Run Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Access at: http://127.0.0.1:8000

📁 Folder Structure

/ LearnEarn  # Main project folder
├── manage.py # Django management script
├── /media # Course files and videos
├── /static # CSS, JS, images
├── /templates # HTML templates
├── /courses # Course app (models, views, URLs)
├── /users # User management
├── /companies # Company management
├── requirements.txt # Project dependencies
└── README.md # Project documentation
