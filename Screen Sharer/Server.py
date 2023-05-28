from vidstream import StreamingServer
import threading

recevier = StreamingServer("192.168.1.107", 1473)

t = threading.Thread(target=recevier.start_server)
t.start()

while input("") != "Stop":
    continue

recevier.stop_server()