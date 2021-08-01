from socket import *

class Transmission():
  def __init__(self):
    self.serverIP = '192.168.0.7'
    self.serverPort = 4308
    pass  
  
  def enviar_objeto(self, original_msg, noise_msg):
    #Se concatena el mensaje original para la comparación
    obj = original_msg + '|' + noise_msg
    print("Enviando-----------------------------")
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(obj.encode(), (self.serverIP, self.serverPort))
    print("-----------------------------Enviado")
    
    pass