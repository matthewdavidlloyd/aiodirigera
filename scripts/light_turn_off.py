import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.hub import Hub


async def turn_off():
    hub = Hub(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'))
    device = await hub.get_device(os.getenv('LIGHT_ID'))

    await device.turn_off()

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(turn_off())
