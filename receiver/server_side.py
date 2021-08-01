from socket import *
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
  #modifiedMessage = message.decode().upper()
  decodeMessage = message.decode()
  
  #transmision layer
  tran.recibir_objeto(decodeMessage)

  print (tran.bit_msg, tran.original_msg)

  #verify layer
  ver.recibir_cadena_segura(tran.bit_msg, tran.original_msg)

  # #app layer  
  # app.recibir_cadena(ver.msg_received)
  
  serverSocket.sendto(decodeMessage.encode(), clientAddres)
