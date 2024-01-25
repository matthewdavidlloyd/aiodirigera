import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.device.light import LightAPI, Light


async def print_state():
    api = LightAPI(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'), os.getenv('LIGHT_ID'))
    device = Light(api)

    await device.update_state()

    print(f"is_on: {device.is_on}")
    print(f"brightness: {device.brightness}")

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(print_state())
