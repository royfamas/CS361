from app import db, User, app
from werkzeug.security import generate_password_hash

def add_user():
    with app.app_context():
        db.create_all()

        # Hardcoded user credentials for testing
        if not User.query.filter_by(username='testuser').first():
            hashed_password = generate_password_hash('testpassword')
            test_user = User(username='testuser', password=hashed_password)
            db.session.add(test_user)
            db.session.commit()
            print("Test user added.")
        else:
            print("Test user already exists.")

if __name__ == '__main__':
    add_user()
