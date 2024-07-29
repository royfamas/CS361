from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from encryption import encrypt_data, decrypt_data
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.LargeBinary, nullable=True)
    phone_number = db.Column(db.LargeBinary, nullable=True)

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
        
        encrypted_email = encrypt_data(email)
        encrypted_phone_number = encrypt_data(phone_number)
        
        user.email = encrypted_email
        user.phone_number = encrypted_phone_number
        
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('update_profile.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    decrypted_email = decrypt_data(user.email) if user.email else "N/A"
    decrypted_phone_number = decrypt_data(user.phone_number) if user.phone_number else "N/A"
    
    return render_template('dashboard.html', email=decrypted_email, phone_number=decrypted_phone_number)

if __name__ == '__main__':
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
