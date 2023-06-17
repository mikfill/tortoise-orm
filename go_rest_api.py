from fastapi import FastAPI
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from models import Users, Posts, Comments, Todos


app = FastAPI()


User_Pydantic = pydantic_model_creator(Users, name="User")

Post_Pydantic = pydantic_model_creator(Posts, name="Post")

Comment_Pydantic = pydantic_model_creator(Comments, name="Comment")

Todo_Pydantic = pydantic_model_creator(Todos, name="Todo")


@app.get("/users")
async def get_all_users():
    return await User_Pydantic.from_queryset(Users.all())


@app.get("/user/{user_id}")
async def get_user_with_id(user_id: int):
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@app.get("/posts")
async def get_all_posts():
    return await Post_Pydantic.from_queryset(Posts.all())


@app.get("/posts/user/{user_id}")
async def get_posts_for_user_with_id(user_id: int):
    return await Post_Pydantic.from_queryset(Posts.filter(user_id=user_id).all())


@app.get("/comments")
async def get_all_comments():
    return await Comment_Pydantic.from_queryset(Comments.all())


@app.get("/todos")
async def get_all_todos():
    return await Todo_Pydantic.from_queryset(Todos.all())


register_tortoise(
    app,
    db_url="sqlite://db.db",
    modules={"models": ["go_rest_api"]},
    # generate_schemas=True,
    add_exception_handlers=True,
)
