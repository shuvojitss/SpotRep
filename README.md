# 🌍 Spot Alert - Community Reporter

A **Flask-based web application** that empowers communities to report and track local issues like potholes, broken streetlights, garbage dumps, and more. Citizens can quickly submit reports with location, category, and optional images. Administrators can view and manage all reports from a central dashboard.

---

## ✨ Features

* 📍 **Location-based reporting**: Users can report issues with latitude & longitude.
* 📝 **Rich issue details**: Title, description, category, and reporter name.
* 🖼️ **Image uploads**: Attach photos of the issue.
* 🗂️ **Categorization**: Tag reports as *Roads*, *Electricity*, *Sanitation*, or *Other*.
* 📊 **Dashboard**: View all submitted issues, sorted by recency.
* 🔐 **Admin Panel**: Manage community issues.
* 💾 **SQLite Database**: Lightweight and easy to set up.

---

## 🛠️ Tech Stack

* **Backend**: [[Flask](https://flask.palletsprojects.com/)] (Python)
* **Database**: SQLite
* **Frontend**: HTML, CSS (custom styling in `static/style.css`)
* **Template Engine**: Jinja2 (`templates/*.html`)
* **Image Handling**: Werkzeug & Flask file upload utilities

---

## 📂 Project Structure

```
community-reporter/
│── app.py              # Main Flask application
│── init_db.sql         # SQL schema for issues table
│── requirements.txt    # Dependencies
│── uploads/            # Uploaded issue images (auto-created)
│── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   └── admin.html
│── static/
│   └── style.css       # Frontend styling
└── README.md           # Project documentation
```

---

## ⚡ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/community-reporter.git
cd community-reporter
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python
>>> from app import init_db
>>> init_db()
>>> exit()
```

### 5. Run the Flask app

```bash
flask run
```

The app will be available at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** 🚀

---

## 🖼️ Screenshots

### HOME PAGE
<img width="1904" height="1009" alt="Screenshot 2025-08-23 225134" src="https://github.com/user-attachments/assets/98ba39ef-f459-4f0c-af79-7100bc955018" />

### DASHBOARD
<img width="1919" height="995" alt="Screenshot 2025-08-23 225153" src="https://github.com/user-attachments/assets/b22900b5-4921-497b-b84a-03c7b3a3684a" />

### ISSUE REPORTING
<img width="1900" height="1009" alt="Screenshot 2025-08-23 225256" src="https://github.com/user-attachments/assets/e5a2a918-eebb-4569-8daa-73f625e51726" />


## 🔮 Future Improvements


* 🌐 Integrate Google Maps for precise location reporting.
* 📧 Email notifications for admins on new reports.
* 📱 Mobile-friendly UI with responsive design.
* 🔑 User authentication (reporters & admins).

---

## 🤝 Contributing

Contributions are welcome! 🎉

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it for your community projects.

---

### 💡 Made with ❤️ by Shuvojit Samanta
