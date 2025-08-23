import os
import sqlite3
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import Flask, g, render_template, request, redirect, url_for, send_from_directory, flash

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
DB_PATH = os.path.join(BASE_DIR, 'issues.db')
ALLOWED_EXT = {'png','jpg','jpeg','gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'dev-secret-key'  # change in prod

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with app.open_resource('init_db.sql') as f:
        db.executescript(f.read().decode('utf8'))
    db.commit()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    db = get_db()
    cur = db.execute('SELECT * FROM issues ORDER BY created_at DESC')
    issues = cur.fetchall()
    return render_template('dashboard.html', issues=issues)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/report', methods=['POST'])
def report_issue():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    category = request.form.get('category', 'Other')
    lat = request.form.get('lat')
    lon = request.form.get('lon')
    reporter = request.form.get('reporter', 'Anonymous')
    status = 'Reported'
    created_at = datetime.utcnow().isoformat(timespec='seconds') + 'Z'

    image_filename = None
    file = request.files.get('photo')
    if file and file.filename != '' and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        filename = f"{timestamp}_{filename}"
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        image_filename = filename

    db = get_db()
    db.execute('''
        INSERT INTO issues (title, description, category, lat, lon, image, reporter, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (title, description, category, lat, lon, image_filename, reporter, status, created_at))
    db.commit()
    flash('Issue reported — thank you!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    if not os.path.exists(DB_PATH):
        with app.app_context():
            init_db()
            print("Initialized DB at", DB_PATH)
    app.run(debug=True)
