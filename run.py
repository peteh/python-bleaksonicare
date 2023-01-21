import sys
import os


import asyncio
from bleak import BleakScanner, BleakClient
from data import SERVICES, PREFIX

uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'
#uuid_active_time_characteristic   = "477ea600-a260-11e4-ae37-0002a5d54010"


async def my_callback(sender, data):
    print("Data received:", data)


async def readServicedata(client, service_uuid, characteristic_uuid):
    #characteristic = await client.find_characteristic(service_uuid, characteristic_uuid)
    data = await client.read_gatt_char(characteristic_uuid)
    print("Data received:" + data.hex())

async def main():
    e = asyncio.Event()
    address = "24:E5:AA:0C:AA:DB"
    async with BleakClient(address) as client:
        for service in client.services:
            print(service)
        # reads the battery level
        battery_level = await client.read_gatt_char(uuid_battery_level_characteristic)
        print(int.from_bytes(battery_level,byteorder='big'))
        #await client.start_notify(uuid_battery_level_characteristic, my_callback)

        
        for service_id in SERVICES:
            service = SERVICES[service_id]
            service_uuid = PREFIX + service_id
            print("Service uuid: " + service_uuid)
            for characteristic_id in service.characteristics:
                characteristic = service.characteristics[characteristic_id]
                print(" " + characteristic.name+": ")
                characteristic_uuid = PREFIX+characteristic_id
                print("  " + characteristic_uuid)
                await readServicedata(client, service_uuid, characteristic_uuid)


        while True:
            await asyncio.sleep(1)

asyncio.run(main())