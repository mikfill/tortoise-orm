from tortoise import Tortoise, run_async

from go_rest_parse import fetch_data
from orm_schema import Comments, Posts, Todos, Users


async def init_database():
    await Tortoise.init(db_url="sqlite://db.db", modules={"models": ["__main__"]})

    await Tortoise.generate_schemas()

    data = await fetch_data()
    users = data[0]["users"]
    posts = data[1]["posts"]
    comments = data[2]["comments"]
    todos = data[3]["todos"]

    del data

    for user_data in users:
        user = await Users(**user_data)
        print(f"Create user: {user}")
        await user.save()

    for post_data in posts:
        post = await Posts(**post_data)
        print(f"Create post: {post}")
        await post.save()

    for comments_data in comments:
        comment = await Comments(**comments_data)
        print(f"Create comment: {comment}")
        await comment.save()

    for todos_data in todos:
        todo = await Todos(**todos_data)
        print(f"Create todo: {todo}")
        await todo.save()

    await Tortoise.close_connections()


run_async(init_database())
