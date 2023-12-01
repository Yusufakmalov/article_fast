from pydantic import BaseModel


class PublicPostValidator(BaseModel):
    user_id: int
    post_name: str
    post_description: str


class EditPostValidator(BaseModel):
    post_id: int
    choice: str
    new_text: str
