import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.device.light import Light
from aiodirigera.hub import Hub


async def turn_on():
    hub = Hub(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'))
    device = Light(hub, os.getenv('LIGHT_ID'))

    await device.turn_on()

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(turn_on())
