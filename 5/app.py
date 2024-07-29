from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=True)  # Changed to String
    phone_number = db.Column(db.String(20), nullable=True)  # Changed to String

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password", 401
    return render_template('login.html')

@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        user = User.query.get(session['user_id'])
        email = request.form['email']
        phone_number = request.form['phone_number']
        
        user.email = email  # Directly store email
        user.phone_number = phone_number  # Directly store phone number
        
        db.session.commit()
        return redirect(url_for('dashboard'))

    # Fetch user info directly without decryption
    user = User.query.get(session['user_id'])
    return render_template('update_profile.html', email=user.email, phone_number=user.phone_number)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    email = user.email if user.email else "N/A"
    phone_number = user.phone_number if user.phone_number else "N/A"
    
    return render_template('dashboard.html', email=email, phone_number=phone_number)

if __name__ == '__main__':
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
