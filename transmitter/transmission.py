from socket import *

class Transmission():
  def __init__(self):
    self.serverIP = '192.168.0.7'
    self.serverPort = 4308
  
  def enviar_objeto(self, original_msg, noise_msg):
    #Se concatena el mensaje original para la comparación
    obj = noise_msg + '|' + original_msg
    print("Enviando-----------------------------")
    print (obj)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(obj.encode(), (self.serverIP, self.serverPort))
    print("-----------------------------Enviado")
    
  