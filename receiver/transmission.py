

class Transmission():
  def __init__(self):
    self.original_msg = ""
    self.bit_msg = ""
    pass

  def recibir_objeto(self, msg):
    message =  msg.split('|')
    #message_bit, message_original = message
    self.bit_msg, self.original_msg = message
    
