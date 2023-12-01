from datetime import datetime

from database import get_db
from database.models import UserArticle



def add_article_db(user_id, article_id, exp_date, article_name, article_number, ):
    db = next(get_db())

    new_article = UserArticle(user_id=user_id, article_id=article_id, article_name=article_name,
                              article_number=article_number, exp_date=exp_date)

    db.add(new_article)
    db.commit()

    return 'Article was successfully added'


def get_exact_user_article_db(user_id):
    db = next(get_db())

    get_exact_user_article = db.query(UserArticle).filter_by(user_id=user_id).first()

    return get_exact_user_article



def check_article_db(user_id, article_number):
    db = next(get_db())

    checker = db.query(UserArticle).filter_by(article_number=article_number, user_id=user_id).first()

    return checker


def delete_article_db(article_id):
    db = next(get_db())

    delete_article = db.query(UserArticle).filter_by(card_id=card_id).first()

    if delete_article:
        db.delete(delete_article)
        db.commit()

        return 'Карта успешно удален'
    else:
        return 'Карта не найдено!'


def check_article_info(user_id, article_name, article_number):
    db = next(get_db())

    checker = db.query(UserArticle).filter_by(article_number=article_number, user_id=user_id,
                                              article_name=article_name)


    return checker

    return {'message': "Not found"}

def validate_article_db(article_name, article_number):
    db = next(get_db())

    validator = db.query(UserArticle).filter_by(article_number=article_number, article_name=article_name)

    if validator:
        return validator
        return "success"
        db.commit()
    else:
        return "something wrong!"

