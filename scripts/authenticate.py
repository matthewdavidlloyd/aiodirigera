import asyncio
import os

from aiohttp import ClientSession
from dotenv import load_dotenv

from aiodirigera.auth import ALPHABET, CODE_LENGTH, random_code, send_challenge, get_token
from aiodirigera.hub import Hub


async def authenticate():
    hub_ip = os.getenv('HUB_IP')

    async with ClientSession() as client_session:
        code_verifier = random_code(ALPHABET, CODE_LENGTH)
        code = await send_challenge(hub_ip, code_verifier, client_session=client_session)

    input("Push button on hub before continuing")

    async with ClientSession() as client_session:
        token = await get_token(hub_ip, code, code_verifier, client_session=client_session)
        print(f"Token: %s", token)

    hub = Hub(hub_ip, token)
    hub_status = await hub.get_hub_status()
    print(hub_status)

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(authenticate())
