import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.hub import Hub


async def turn_on():
    hub = Hub(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'))

    devices = await hub.get_devices()

    [print(device) for device in devices]

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(turn_on())
