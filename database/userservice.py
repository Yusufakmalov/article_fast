from database.models import User

from database import get_db

from datetime import datetime


def register_user_db(name, surname, email, phone_number, city, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return True
    new_user = User(name=name, surname=surname, email=email,
                    phone_number=phone_number, city=city, password=password,
                    reg_date=datetime.now())
    db.add(new_user)
    db.commit()

    return 'Successfully'


def login_user_db(email, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Incorrect password!'
    else:
        return "Mistake in data"
    login_user = User(email=email, password=password)
    db.add(login_user)
    db.commit()

# Get all users
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users

def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    return exact_user