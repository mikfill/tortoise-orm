import asyncio

from tortoise import Tortoise, run_async

from go_rest_parse import BASE_URL, fetch_data
from orm_schema import Comments, Posts, Todos, Users


async def init_database():
    await Tortoise.init(db_url="sqlite://db.db", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    try:
        data = await asyncio.wait_for(fetch_data(), timeout=10)
    except asyncio.TimeoutError:
        print(f"fetch data from {BASE_URL} took too long to execution.")
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
        Todos.bulk_create(todo_objs)
    )

    await Tortoise.close_connections()

asyncio.run(init_database())
