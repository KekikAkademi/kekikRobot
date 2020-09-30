# https://github.com/pokurt/Nana-Remix

import aiohttp

async def deldog(message, data):
    BASE_URL = 'https://nekobin.com'
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{BASE_URL}/api/documents', json={"content":data}, timeout=3) as response:
            key = (await response.json())["result"]["key"]
            reply = f'{BASE_URL}/raw/{key}'
    return reply