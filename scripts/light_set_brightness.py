import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.hub import Hub


async def set_brightness():
    hub = Hub(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'))
    device = await hub.get_device(os.getenv('LIGHT_ID'))

    await device.set_brightness(100)

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(set_brightness())
