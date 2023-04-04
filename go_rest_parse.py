import asyncio
import json
import httpx


BASE_URL = "https://gorest.co.in/public/v2/"


async def get_users(client):
    url = BASE_URL + "users"
    resp = await client.get(url)
    return {"users": resp.json()}


async def get_posts(client):
    url = BASE_URL + "posts"
    resp = await client.get(url)
    return {"posts": resp.json()}


async def get_comments(client):
    url = BASE_URL + "comments"
    resp = await client.get(url)
    return {"comments": resp.json()}


async def get_todos(client):
    url = BASE_URL + "todos"
    resp = await client.get(url)
    return {"todos": resp.json()}


async def fetch_data() -> list[dict]:
    """Parse data from https://gorest.co.in/

    Returns:
        A list dicts with data for users and their posts.
    """
    result = []
    async with httpx.AsyncClient() as c:
        tasks = []
        tasks.append(asyncio.create_task(get_users(client=c)))
        tasks.append(asyncio.create_task(get_posts(client=c)))
        tasks.append(asyncio.create_task(get_comments(client=c)))
        tasks.append(asyncio.create_task(get_todos(client=c)))

        result = await asyncio.gather(*tasks)

    return result


#print(json.dumps(asyncio.run(fetch_data()), indent=1))
