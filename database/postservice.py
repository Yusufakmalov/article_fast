from .models import UserArticle
from datetime import datetime

from database import get_db

# Adding posts
def post_db(user_id, post_text):
    db = next(get_db())

    new_post = UserArticle(user_id=user_id, post_text=post_text, publish_date=datetime.now())

    db.add(new_post)
    db.commit()

    return "Successfully Added"



def edit_post_db(post_id, user_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserArticle).filter_by(id=post_id, user_id=user_id).first()

    if exact_post:
        exact_post.post_text = new_text
        db.commit()

        return 'Successfully changed'
    else:
        return False

def delete_post_db(post_id):
    db = next(get_db())

    delete_post = db.query(UserArticle).filter_by(id=post_id).first()


    if delete_post:
        db.delete(delete_post)
        db.commit()

        return 'successfully deleted'
    else:
        return False

