# MRE Example
import asyncio
import aiohttp


class MreMeal:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/todos/1"
        self.session = aiohttp.ClientSession()

    async def fetch(self):
        async with self.session.get(self.url) as response:
            return await response.json()

