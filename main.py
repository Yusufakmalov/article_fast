from fastapi import FastAPI

from user.user_api import user_router
from post_article.post_article_api import posts_router
from article.article_api import coms_router

from database import Base, engine
Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(posts_router)
app.include_router(coms_router)



@app.get('/home')
async def home():
    return {'message': 'Hello bitch!'}

