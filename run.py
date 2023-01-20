import sys
import os


import asyncio
from bleak import BleakScanner, BleakClient

uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'

async def main():
    
    address = "24:E5:AA:0C:AA:DB"
    async with BleakClient(address) as client:
        svcs = await client.get_services()
        # reads the battery level
        battery_level = await client.read_gatt_char(uuid_battery_level_characteristic)
        print(int.from_bytes(battery_level,byteorder='big'))

asyncio.run(main())