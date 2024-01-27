import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.hub import Hub


async def print_state():
    hub = Hub(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'))
    device = await hub.get_device(os.getenv('LIGHT_ID'))

    await device.update_state()

    print(f"is_on: {device.is_on}")
    print(f"brightness: {device.brightness}")

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(print_state())
