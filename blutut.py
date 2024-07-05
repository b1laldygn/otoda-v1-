import asyncio
from bleak import BleakScanner

async def tarama():
    cihazlar = await BleakScanner.discover()
    for cihaz in cihazlar:
        print(f"Cihaz Adı: {cihaz.name}, MAC Adresi: {cihaz.address}")

asyncio.run(tarama())
