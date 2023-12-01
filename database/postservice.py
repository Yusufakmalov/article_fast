from .models import Post, User
from datetime import datetime

from database import get_db


# Adding posts
def post_db(user_id, post_name, post_description):
    db = next(get_db())

    new_post = db.query(User).filter_by(user_id=user_id).first()

    if new_post:
        new_post_add = Post(user_id=user_id, post_name=post_name, post_description=post_description,
                            exp_date=datetime.now())
        db.add(new_post_add)
        db.commit()
        return f"Successfully Added id - {new_post_add.id}"

    else:
        return 'Error'


def edit_post_db(post_id, choice, new_text):
    db = next(get_db())

    exact_post = db.query(Post).filter_by(id=post_id).first()

    if exact_post:
        if choice == 'post_name':
            exact_post.post_name = new_text
            db.commit()
            return 'Successfully changed'
        elif choice == 'post_description':
            exact_post.post_description = new_text
            db.commit()
            return 'Successfully changed'
    else:
        return {'status': 0, 'message': 'Post Denied'}


def delete_post_db(post_id):
    db = next(get_db())

    delete_post = db.query(Post).filter_by(id=post_id).first()

    if delete_post:
        db.delete(delete_post)
        db.commit()

        return 'successfully deleted'
    else:
        return False


def get_all_posts_db():
    db = next(get_db())

    result = db.query(Post).all()

    return result


def get_exact_post_db(post_id):
    db = next(get_db())

    result = db.query(Post).filter_by(id=post_id).first()

    return result

