from vidstream import ScreenShareClient
import threading

client = ScreenShareClient("192.168.1.107", 1473)

t = threading.Thread(target=client.start_stream)
t.start()

while input("") != "Stop":
    continue

client.start_stream()