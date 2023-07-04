import asyncio
from typing import List
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from starlette.responses import RedirectResponse


from parse import BASE_URL, fetch_data
from models import (
    Comment_Pydantic,
    Comments,
    Post_Pydantic,
    Posts,
    Todo_Pydantic,
    Todos,
    User_Pydantic,
    Users,
)

DB_PATH = "db.db"

app = FastAPI()


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/init-db")
async def initialize_database():
    await init_database()
    return {"message": "Database initialization completed."}


@app.get("/users", response_model=List[User_Pydantic])
async def get_all_users():
    return await User_Pydantic.from_queryset(Users.all())


@app.get(
    "/user/{user_id}",
    response_model=User_Pydantic,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_user_with_id(user_id: int):
    return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


@app.get("/posts", response_model=List[Post_Pydantic])
async def get_all_posts():
    return await Post_Pydantic.from_queryset(Posts.all())


@app.get(
    "/posts/user/{user_id}",
    response_model=List[Post_Pydantic],
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_posts_for_user_with_id(user_id: int):
    return await Post_Pydantic.from_queryset(Posts.filter(user_id=user_id).all())


@app.get("/comments", response_model=List[Comment_Pydantic])
async def get_all_comments():
    return await Comment_Pydantic.from_queryset(Comments.all())


@app.get("/todos", response_model=List[Todo_Pydantic])
async def get_all_todos():
    return await Todo_Pydantic.from_queryset(Todos.all())


register_tortoise(
    app,
    db_url=f"sqlite://{DB_PATH}",
    modules={"models": ["models"]},
    add_exception_handlers=True,
)


async def init_database():
    await Tortoise.init(db_url=f"sqlite://{DB_PATH}", modules={"models": ["models"]})
    await Tortoise.generate_schemas()

    try:
        data = await asyncio.wait_for(fetch_data(), timeout=5)
    except asyncio.TimeoutError:
        print(f"Fetching data from {BASE_URL} took too long to execute.")
        return

    users = data[0]["users"]
    posts = data[1]["posts"]
    comments = data[2]["comments"]
    todos = data[3]["todos"]

    user_objs = [Users(**user_data) for user_data in users]
    post_objs = [Posts(**post_data) for post_data in posts]
    comment_objs = [Comments(**comment_data) for comment_data in comments]
    todo_objs = [Todos(**todo_data) for todo_data in todos]

    await asyncio.gather(
        Users.bulk_create(user_objs),
        Posts.bulk_create(post_objs),
        Comments.bulk_create(comment_objs),
        Todos.bulk_create(todo_objs),
    )

    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(init_database())
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
