from pydantic import BaseModel

class ArticleModel(BaseModel):
    article_text: str
    user_id: int
    post_id: int


class EditArticleModel(BaseModel):
    new_text: str
    article: int
