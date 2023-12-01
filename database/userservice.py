from database.models import User

from database import get_db

from datetime import datetime


def register_user_db(name, surname, email, phone_number, city, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if not checker:
        new_user = User(name=name, last_name=surname, email=email,
                        phone_number=phone_number, city=city, password=password,
                        reg_date=datetime.now())

        db.add(new_user)
        db.commit()

        return 'Successfully'
    else:
        return 'successfully'


def login_user_db(email, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()

    if not checker:
        login_user = User(email=email, password=password)

        db.add(login_user)
        db.commit()

        return "Successfully"
    else:
        return "successfully"


# Get all users
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    if all_users:
        return all_users
    else:
        return "Successfully"


def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        return exact_user
    else:
        return "Successfully"


def delete_user_db(user_id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(user_id=user_id).first()

    if delete_user:
        return delete_user
    else:
        return "Successfully"


def edit_user_db(user_id):
    db = next(get_db())

    edit_user = db.query(User).filter_by(user_id=user_id).first()

    if edit_user:
        return edit_user
    else:
        return "Successfully"
