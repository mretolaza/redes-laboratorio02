from socket import *
from transmission import Transmission
from verify import Verify
from app import App

serverPort = 4308
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))

print("Listen...")

tran = Transmission()
ver = Verify("HAM") # "HAM" para el algoritmo de hammilton, "CRC32" para el algoritmo CRC-32
app = App()

while True: 
  message, clientAddres = serverSocket.recvfrom(2048)
  decodeMessage = message.decode()
  
  #transmision layer
  tran.recibir_objeto(decodeMessage)

  #print (tran.bit_msg, tran.original_msg)

  #verify layer
  ver.recibir_cadena_segura(tran.bit_msg, tran.original_msg)

  # #app layer  
  app.recibir_cadena(ver.msg_rec)
  
  serverSocket.sendto(decodeMessage.encode(), clientAddres)
