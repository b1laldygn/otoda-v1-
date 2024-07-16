import bluetooth
import subprocess
import time

target_name = "KTOOLS AIRTONES" 
target_address = None

nearby_devices = bluetooth.discover_devices()
for addr in nearby_devices:
    name = bluetooth.lookup_name(addr)
    print(f"{addr}: {name}")
    if target_name == name:
        target_address = addr
        break

if target_address is None:
    print("Cihaz bulunamadı")
    quit()

print("Hedef cihazın adresi:", target_address)
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1 
sock.connect((target_address, port))

print("Kulaklığa bağlantı başarılı.")
try:
    while True:
        data = b"Hello, Bluetooth World!" 
        sock.send(data)
        time.sleep(1)  
except KeyboardInterrupt:
    pass
sock.close()
print("Bağlantı kapatıldı.")
