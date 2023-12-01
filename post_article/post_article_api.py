from fastapi import APIRouter, UploadFile, Body

from post_article import PublicPostValidator, EditPostValidator

from database.postservice import edit_post_db, delete_post_db, post_db

posts_router = APIRouter(prefix='/user_post', tags=['work with publications'])

@posts_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    result = post_db(**data.model_dump())

    return {'message': result}


@posts_router.put('/change_post')
async def change_post(data: EditPostValidator):
    result = edit_post_db(**data.model_dump())

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
async def get_all_posts(post_id: int):
    result = edit_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}
@posts_router.get('/get_exact_post')
async def get_exact_post(post_id: int):
    result = get_exact_post(post_id)

    if result:
        return {'message': result}
    else:
        return 'Post not found'
