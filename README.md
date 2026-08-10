# 💰 Expense Tracker

A modern, responsive, and feature-rich **Expense Tracker Web Application** built with **Flask**, **Python**, **SQLite**, **HTML**, **CSS**, and **JavaScript**. It helps users manage their personal finances by tracking income and expenses, analyzing spending habits, and visualizing financial data through an intuitive dashboard.

> 🚧 **Project Status:** Currently under active development.

---

# ✨ Features

### Current Features

* Modern Landing Page
* Responsive Navigation Bar
* Professional UI Design
* Modular Flask Project Structure
* Application Factory Pattern
* Blueprint Architecture
* Configuration Management

### Planned Features

* Secure User Authentication
* Dashboard Analytics
* Income & Expense Management
* Categories & Tags
* Monthly & Yearly Reports
* Budget Planning
* Interactive Charts
* Search & Filters
* Dark Mode
* User Profile & Settings
* Data Export (CSV/PDF)
* Mobile Responsive Design

---

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite
* SQLAlchemy

### Tools

* Git
* GitHub
* VS Code

---

# 📂 Project Structure

```text
expense-tracker/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   ├── models/
│   ├── templates/
│   ├── static/
│   └── utils/
│
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

# 📅 Development Progress

## ✅ Day 1

* Project initialization
* Git & GitHub setup
* Flask installation
* Initial project configuration

## ✅ Day 2

* Landing page design
* Responsive navigation bar
* Footer section
* Frontend folder structure

## ✅ Day 3

* Flask Application Factory
* Blueprint Architecture
* Configuration Management
* Professional project structure

## ✅ Day 4 Progress

- Configured SQLite database
- Integrated SQLAlchemy
- Added Flask-Migrate
- Created User model
- Created Expense model
- Generated initial database migration

### ✅ Day 5 — User Registration & Authentication Foundation

Implemented the initial authentication module and secure user registration workflow.

#### Completed

- Added Flask-Login integration
- Added Flask-WTF form handling
- Added CSRF protection
- Created modular authentication Blueprint
- Implemented registration form validation
- Added username format validation
- Added email validation
- Added duplicate username detection
- Added duplicate email detection
- Implemented secure password hashing
- Added database transaction handling
- Added rollback handling for registration failures
- Created responsive registration interface
- Added reusable flash notifications
- Improved application factory organization

## ✅ Day 6 — Authentication & Session Management

### Completed

- Integrated Flask-Login with the User model
- Added Flask-Login user loader
- Implemented login form
- Implemented secure login workflow
- Added password verification
- Added Remember Me functionality
- Implemented logout using POST
- Added protected dashboard route
- Added `@login_required`
- Added authentication-aware navigation
- Added login/logout feedback messages
- Tested authentication workflow


## Day 7 — Expense Management Foundation

### Completed

- Designed Expense database model
- Added User → Expense relationship
- Added expense database migration
- Created ExpenseForm
- Added server-side validation
- Created Expense blueprint
- Implemented secure expense creation
- Added expense listing
- Added protected expense routes
- Added dashboard expense actions
- Implemented user-specific expense filtering
- Tested expense ownership isolation


## Day 8 — Expense CRUD

### Completed

- Added expense editing
- Added expense deletion
- Added reusable expense forms
- Added CSRF protection
- Added POST-only deletion
- Added expense ownership authorization
- Added edit and delete UI actions
- Tested CRUD functionality
- Tested cross-user resource protection

### Expense CRUD

| Operation | Endpoint | Method |
|---|---|---|
| Create | `/expenses/add` | GET/POST |
| Read | `/expenses/` | GET |
| Update | `/expenses/<id>/edit` | GET/POST |
| Delete | `/expenses/<id>/delete` | POST |



# 🚀 Roadmap

* [ ] User Authentication
* [ ] Expense CRUD
* [ ] Income Management
* [ ] Categories
* [ ] Dashboard Analytics
* [ ] Charts & Reports
* [ ] Budget Planner
* [ ] Search & Filtering
* [ ] Profile Management
* [ ] Settings
* [ ] Deployment
* [ ] Automated Testing

---

# 📸 Screenshots

> Screenshots will be added as the project progresses.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Priya Kumari Gupta**

Bachelor of Information Technology (BIT)

Tribhuvan University, Nepal

⭐ If you find this project helpful, consider giving it a star on GitHub.
