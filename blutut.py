import bluetooth
devices = bluetooth.discover_devices(lookup_names=True)
for addr, name in devices:
    print("ad: {}, adres: {}".format(name, addr))
