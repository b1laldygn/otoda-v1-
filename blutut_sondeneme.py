import bluetooth

def list_bluetooth_devices():
    print("Bluetooth cihazları aranıyor...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    print("Bulunan cihazlar:")
    for addr, name in devices:
        print(f"Adres: {addr}, İsim: {name}")
    return devices

def connect_to_device(target_name):
    devices = list_bluetooth_devices()
    target_address = None

    for addr, name in devices:
        if target_name == name:
            target_address = addr
            break

    if target_address is not None:
        print(f"{target_name} cihazına bağlanılıyor ({target_address})...")
        # Burada RFCOMM soketi oluşturuyoruz
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_address, 1))
        print(f"{target_name} cihazına başarıyla bağlanıldı!")
        return sock
    else:
        print(f"{target_name} cihazı bulunamadı.")
        return None

if __name__ == "__main__":
    target_device_name = "KTOOLS AIRTONES"  # Bağlanmak istediğiniz cihazın ismini buraya yazın
    sock = connect_to_device(target_device_name)
    if sock:
        # Bağlantı başarılıysa, burada veri gönderme/alma işlemlerini yapabilirsiniz
        # Örnek olarak bir mesaj gönderelim
        sock.send("Merhaba, bu bir test mesajıdır.")
        sock.close()