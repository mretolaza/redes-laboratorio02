from socket import *
from sys import tracebacklimit
from transmission import Transmission
from verify import Verify
from app import App

serverPort = 4308
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("Listen...")

tran = Transmission()
ver = Verify()
app = App()

while True: 
  message, clientAddres = serverSocket.recvfrom(2048)
  #transmision layer
  tran.recibir_objeto(message)

  #verify layer
  ver.recibir_cadena_segura(tran.recibed_msg)

  #app layer  
  app.recibir_cadena(ver.msg_received)
  


