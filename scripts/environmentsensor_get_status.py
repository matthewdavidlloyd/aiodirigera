import asyncio
import os

from dotenv import load_dotenv

from aiodirigera.device import DeviceAPI
from aiodirigera.device.sensor import EnvironmentSensor


async def print_state():
    api = DeviceAPI(os.getenv('HUB_IP'), os.getenv('HUB_TOKEN'), os.getenv('ENVIRONMENTSENSOR_ID'))
    device = EnvironmentSensor(api)

    await device.update_state()

    print(f"temperature: {device.temperature}")
    print(f"humidity: {device.humidity}")

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(print_state())
