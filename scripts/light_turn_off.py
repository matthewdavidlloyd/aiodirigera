import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.device.light import LightAPI, Light


async def turn_off():
    api = LightAPI(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'), os.getenv('LIGHT_ID'))
    device = Light(api)

    await device.turn_off()

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(turn_off())

