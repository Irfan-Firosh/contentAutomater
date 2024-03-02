import os

def connect(router_name):
    #os.system('cmd /c "netsh wlan show networks"')
    os.system(f'''cmd /c "netsh wlan connect name={router_name}"''')

user = "1"

u = user + "2"

print(u)