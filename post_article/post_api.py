from fastapi import APIRouter

from post_article import PublicPostValidator, EditPostValidator

from database.postservice import post_db, edit_post_db, get_all_posts_db, delete_post_db, get_exact_post_db

posts_router = APIRouter(prefix='/user_post', tags=['work with publications'])


@posts_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    model = data.model_dump()

    result = post_db(**model)

    return {'message': result}


@posts_router.post('/edit_post')
async def change_post(data: EditPostValidator):
    model = data.model_dump()

    result = edit_post_db(**model)
    if result:
        return {'message': result}
    else:
        return {'message': "not found"}


@posts_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': "post not found"}


@posts_router.get('/get_all_posts')
async def get_all_posts():
    result = get_all_posts_db()
    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}


@posts_router.get('/get_exact_post')
async def get_exact_post(post_id: int):
    result = get_exact_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return 'Post not found'
