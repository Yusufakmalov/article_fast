from fastapi import APIRouter

from article import ArticleModel, EditArticleModel

from database.article_service import add_article_db, validate_article_db, delete_article_db, get_exact_user_article_db

coms_router = APIRouter(prefix='/article', tags=['work with article'])

@coms_router.post('/add_article')
async def add_article(data: ArticleModel):
        result = add_article_db(**data.model_dump())

        return {'message': result}

        return {'message': 'successfully added'}

@coms_router.put('/edit_article')
async def change_article(data: EditArticleModel):
        result = validate_article_db(**data.model_dump())

        return {'message': result}

        return {'message': 'successfully validated'}

@coms_router.delete('/delete_article')
async def delete_article(article_id: int):
        result = delete_article_db(article_id=article_id)

        return {'message': result}

        return {'message': 'successfully deleted'}

@coms_router.get('/get_article')
async def get_article(post_id: int):
    result = get_exact_user_article_db(post_id=post_id)

    return {'message': result}

    return {'message': 'successfully got'}