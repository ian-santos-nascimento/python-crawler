import queue
import threading
import requests

q = queue.Queue()
valid_proxies = queue.Queue()

with open("../proxy_ip_list", 'r') as f:
    proxies = f.read().split("\n")
    for line in proxies:
        q.put(line)


def check_proxy_conexion():
    print("check_proxy_conexion AQUI")
    global q
    global valid_proxies
    while not q.empty():
        proxy = q.get()
        try:
            response = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy})
        except:
            continue
        if response.status_code == 200:
            valid_proxies.put(proxy)
            print(proxy)

for _ in range(10):
    threading.Thread(target=check_proxy_conexion()).start()
